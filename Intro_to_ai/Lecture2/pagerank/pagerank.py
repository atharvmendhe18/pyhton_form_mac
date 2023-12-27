import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(link for link in pages[filename] if link in pages)

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    transtion_model_dict = {}
    links_in_page = corpus[page]
    if len(links_in_page) != 0:
        prob_of_each_page = damping_factor / len(links_in_page)
        for link in links_in_page:
            transtion_model_dict[link] = prob_of_each_page
        prob_of_corpus = (1 - damping_factor) / len(corpus)
        for link in corpus:
            if link not in transtion_model_dict:
                transtion_model_dict[link] = prob_of_corpus
            else:
                transtion_model_dict[link] += prob_of_corpus

            return transtion_model_dict

    else:
        prob_of_corpus = 1 / len(corpus)
        for link in corpus:
            transtion_model_dict[link] = prob_of_corpus
        return transtion_model_dict

    raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    page = random.choice(list(corpus))
    page_rank = {}
    # initilize the count of all the pages to 0
    for page in corpus:
        page_rank[page] = 0

    for _ in range(n):
        transtionmodel = transition_model(corpus, page, damping_factor)
        pages = []
        prob_pages = []
        for page in list(transtionmodel):
            pages.append(page)
            prob_pages.append(transtionmodel[page])
        page = random.choices(pages, prob_pages, k=1)
        page = page[0]

        page_rank[page] += 1

    for pager in page_rank:
        page_rank[pager] = page_rank[pager] / n

    return page_rank

    raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_rank = {}
    start_page_rank = 1 / len(corpus)
    for pagec in corpus:
        page_rank[pagec] = start_page_rank
    for _ in range(100):
        for pagec in corpus:
            two_sum = 0

            for page_i in corpus:
                if pagec in corpus[page_i]:
                    num_links_i = len(corpus[page_i])
                    two_sum += page_rank[page_i] / num_links_i

            two_sum = damping_factor * two_sum
            two_sum += (1 - damping_factor) / len(corpus)
            page_rank[pagec] = two_sum

    return page_rank

    raise NotImplementedError


if __name__ == "__main__":
    main()
