import csv
import itertools
import sys


PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}

def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }
    print(people)
    print()
    print(probabilities)
    print()
    print(joint_probability(people,{"Harry"}, {"James"}, {"James"}))
    update(probabilities,{"Harry"}, {"James"}, {"James"},joint_probability(people,{"Harry"}, {"James"}, {"James"}))
    print(probabilities)

def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }      
    return data    


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    calculated_probabilties = []
    zero_genes = set({})
    jointprobability = 1
    for name in people:
        if name not in one_gene and name not in two_genes:
            zero_genes.add(name)
    
    for name in zero_genes:
        if people[name]["father"] == None and people[name]["mother"] == None:
            if name in have_trait:
                prob = (PROBS["gene"][0] * PROBS["trait"][0][True])
                calculated_probabilties.append(prob)
            else:
                prob = (PROBS["gene"][0] * PROBS["trait"][0][False])
                calculated_probabilties.append(prob)

        else:
            # in this case we need to calulate what is the probability of zero genes given parents have-- 
            # --whatever no of genes given in this case
            # in this case prob_mother_zero and prob_father_zero is the probability each of them passes zero genes to their offspirng
            if people[name]["father"] in one_gene:
                prob_father_zero = (0.5)
            elif people[name]["father"] in two_genes: # i dont know if this is correct or not
                prob_father_zero = (PROBS["mutation"]) 
            else:
                prob_father_zero = (1 - PROBS["mutation"])

            if people[name]["mother"] in one_gene:
                prob_mother_zero = (0.5)
            elif people[name]["mother"] in two_genes: # i dont know if this is correct or not
                prob_mother_zero = (PROBS["mutation"]) 
            else:
                prob_mother_zero = (1 - PROBS["mutation"])   

            if name in have_trait:
                prob  = (prob_father_zero * prob_mother_zero * PROBS["trait"][0][True])
                calculated_probabilties.append(prob)
            else:
                prob  = (prob_father_zero * prob_mother_zero * PROBS["trait"][0][False])
                calculated_probabilties.append(prob)

    for name in one_gene:
        if people[name]["father"] == None and people[name]["mother"] == None:
            if name in have_trait:
                prob = (PROBS["gene"][1] * PROBS["trait"][1][True])
                calculated_probabilties.append(prob)
            else:
                prob = (PROBS["gene"][1] * PROBS["trait"][1][False])
                calculated_probabilties.append(prob)
        else:
            if people[name]["father"] in one_gene:
                prob_father_one = (0.5)
            elif people[name]["father"] in two_genes:
                prob_father_one = (1 - PROBS["mutation"]) 
            else:
                prob_father_one = (PROBS["mutation"])

            if people[name]["mother"] in one_gene:
                prob_mother_one = (0.5)
            elif people[name]["mother"] in two_genes:
                prob_mother_one = (1 - PROBS["mutation"]) 
            else:
                prob_mother_one = (PROBS["mutation"])    

            if name in have_trait:
                prob = (((prob_father_one) * (1- prob_mother_one)) + ((1 - prob_father_one) * (prob_mother_one)))
                calculated_probabilties.append(prob * PROBS["trait"][1][True])
            else:
                prob = (((prob_father_one) * (1- prob_mother_one)) + ((1 - prob_father_one) * (prob_mother_one)))
                print(prob)
                calculated_probabilties.append(prob * PROBS["trait"][1][False])
                
    for name in two_genes:
        if people[name]["father"] == None and people[name]["mother"] == None:
            if name in have_trait:
                prob  = (PROBS["gene"][2] * PROBS["trait"][2][True])
                calculated_probabilties.append(prob)
            else:
                prob  = (PROBS["gene"][2] * PROBS["trait"][2][False])
                calculated_probabilties.append(prob)

        else:
            # what we need is the probability of each parent passing one gene to their offspiring--
            # -- so we can get the values of parent passing one gene form above for loop of one gene
            
            if name in have_trait:
                prob = (((prob_father_one) * (prob_mother_one)))
                calculated_probabilties.append(prob  * PROBS["trait"][2][True])
            else:
                prob = (((prob_father_one) * (prob_mother_one)) )
                calculated_probabilties.append(prob * PROBS["trait"][2][False])


    for probability in calculated_probabilties:
        jointprobability = jointprobability * probability

    return jointprobability    

            
    #   if people[name]["father"] != None and people[name]["mother"] != None:

    #         if people[name]["father"] == 0:
    #             prob_zero_father = PROBS["trait"][0][True]
    #             prob_one_father = PROBS["trait"][1][True]
    #             prob_two_father = PROBS["trait"][2][True]
    #         else:
    #             prob_zero_father = PROBS["trait"][0][False]
    #             prob_one_father = PROBS["trait"][1][False]
    #             prob_two_father = PROBS["trait"][2][False]

    #         if people[name]["mother"] == 0:
    #             prob_zero_mother = PROBS["trait"][0][True]
    #             prob_one_mother = PROBS["trait"][1][True]
    #             prob_two_mother = PROBS["trait"][2][True]
    #         else:
    #             prob_zero_mother = PROBS["trait"][0][False]
    #             prob_one_mother = PROBS["trait"][1][False]
    #             prob_two_mother = PROBS["trait"][2][False]


    #         prob_zeo_list[i] = ((prob_zero_father * prob_zero_mother) +  (0.5 * prob_zero_father * prob_one_mother) +
    #                              ( 0.5 * prob_one_father * prob_zero_mother)  ( PROBS["mutation"] * 0.5 * prob_zero_father * prob_one_mother) +
    #                                ( PROBS["mutation"] * 0.5 * prob_one_father * prob_zero_mother) ())
    
    # if name not in have_trait:
    #             if people[name]['mother'] == None and people[name]['father'] == None:
    #                 zero_gene = PROBS["gene"][0]
    #                 zero
                    

    raise NotImplementedError


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """

    zero_gene = []
    for name in probabilities:
        if name not in one_gene and name not in two_genes:
            zero_gene.append(name)

    for name in zero_gene:
        probabilities[name]["gene"][0] += p

    for name in one_gene:
        probabilities[name]["gene"][1] += p

    for name in two_genes:
        probabilities[name]["gene"][2] += p

    if name in have_trait:
        probabilities[name]["trait"][True] += p
    else:
        probabilities[name]["trait"][False] += p    
       

    # i have repeted a lot of lines of code in this function the only things changing are arrays and numbers 0,1,2; there has to be a better way to do this

def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """

    for name in probabilities:
        # normalizing gene
        x = (1.00 /(probabilities[name]["gene"][0] + probabilities[name]["gene"][1] + probabilities[name]["gene"][2]))
        for i in range(3):
            probabilities[name]["gene"][i] *= x

        # normalizing trait
        y = ( 1.00 / (probabilities[name]["trait"][True] + probabilities[name]["trait"][False]))  

        probabilities[name]["trait"][True] *= y
        probabilities[name]["trait"][False] *= y
    

if __name__ == "__main__":
    main()