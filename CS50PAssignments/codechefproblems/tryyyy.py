import random

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
        prob_of_corpus = 1/len(corpus)
        for link in corpus:
            transtion_model_dict[link] = prob_of_corpus
        return transtion_model_dict      


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
    #initilize the count of all the pages to 0
    for pagec in corpus:
        page_rank[pagec] = 0
    
    for _ in range(n):
        transtionmodel = transition_model(corpus, page, damping_factor)
        pages = []
        prob_pages = []
        for paget in list(transtionmodel):
            pages.append(paget)
            prob_pages.append(transtionmodel[paget])
            
        page  = random.choices(pages, prob_pages, k=1)
        page = page[0]
       
        page_rank[page] += 1   

    for pager in page_rank:
        page_rank[pager] = page_rank[pager]/n     

    return page_rank          



def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_rank = {}
    start_page_rank = 1/len(corpus)
    for pagec in corpus:
            page_rank[pagec] = start_page_rank
    print(f"Start page rank for each page is {page_rank}")
    for _ in range(3):
        print(f"{_}st iteration started")
        for pagec in corpus:
            two_sum = 0
            print(f"page choosen was {pagec}")
            for page_i in corpus:
                if pagec in corpus[page_i]:
                    num_links_i = len(corpus[page_i])
                    print(f"no of links in page i is {num_links_i}")
                   
                    two_sum += page_rank[page_i]/num_links_i
                    print(two_sum)

            two_sum = damping_factor * two_sum
            two_sum += (1 - damping_factor)/len(corpus) 
            print(f"iterated page rank is {two_sum}")
            page_rank[pagec]  = two_sum 
            print(page_rank)

    return page_rank   


    

    raise NotImplementedError


def main():
    corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}
    damping = 0.85

    print(sample_pagerank(corpus,damping,10000))
    print(iterate_pagerank(corpus,damping))
    

if __name__ == "__main__":
    main()    
