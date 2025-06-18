from collections import defaultdict

def apriori(dataset,min_support,min_confidence):
    item_counts=defaultdict(int)
    for transaction in dataset:
        for item in transaction:
            item_counts[item]+=1
            
    num_transactions=len(dataset)
    frequent_1_itemsets=set()
    for item,count in item_counts.items():
        if count/num_transactions>=min_support:
            frequent_1_itemsets.add(frozenset([item]))
            
    frequent_itemsets=[frequent_1_itemsets]
    k=2
    while True:
        candidate_itemsets=set()
        for i in range(len(frequent_itemsets[-1])):
            for j in range(len(frequent_itemsets[-1])):
                itemset1=list(frequent_itemsets[-1])[i]
                itemset2=list(frequent_itemsets[-1])[j]
                united_itemset=itemset1.union(itemset2)
                if(len(united_itemset))==k:
                    candidate_itemsets.add(united_itemset)
        itemset_counts=defaultdict(int)
        for transaction in dataset:
            for candidate in candidate_itemsets:
                if candidate.issubset(set(transaction)):
                    itemset_counts[candidate]+=1
        frequent_k_itemsets=set()
        for itemset,count in itemset_counts.items():
            if count/num_transactions>=min_support:
                frequent_k_itemsets.add(itemset)
        if not frequent_k_itemsets:
            break
        frequent_itemsets.append(frequent_k_itemsets)
        k+=1
        
    rules=[]
    for itemset in frequent_itemsets:
        for itemset in itemset:
            if(len(itemset))>1:
                for antecednt in itemset:
                    consequent=itemset.difference(set([antecednt]))
                    confidence=support_count(itemset,dataset)/support_count(set([antecednt]),dataset)
                    support=support_count(itemset,dataset)/num_transactions
                    if confidence>=min_confidence:
                        rules.append((set([antecednt]),consequent,confidence,support))
    return frequent_itemsets,rules
def support_count(itemset, dataset):
    count=0
    for transaction in dataset:
        if itemset.issubset(set(transaction)):
            count=+1
    return count
dataset=[['A','B','C','D'],['B','C','E'],['A','B','C','E'],['B','D','E'],['A','B','C','D']]
min_support=0.5
min_confidence=0.6
frequent_itemsets,rules=apriori(dataset, min_support, min_confidence)
print("Frequent itemsets: ")
for itemset_level in frequent_itemsets:
    for itemset in itemset_level:
        print(itemset)
print('\nASSOCIATION RULE :')
for antecednt,consequent,confidence,support in rules:
    print(f"{antecednt} => {consequent}(Confidence:{confidence:.2f},Support:{support:.2f})")
