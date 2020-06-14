import requests
from bs4 import BeautifulSoup as bs
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

oneplus_reviews=[]

for i in range(1,31):
    op=[]
    url="https://www.amazon.in/OnePlus-Mirror-Black-128GB-Storage/product-reviews/B07DJHV6VZ/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="+ str(i)
    response=requests.get(url)
    soup= bs(response.content,"html.parser")
    reviews = soup.find_all("span",attrs={"class","a-size-base review-text review-text-content"})
    
    for i in range(len(reviews)):
        op.append(reviews[i].text)
    
    oneplus_reviews = oneplus_reviews + op

#writing reviews in text file

with open("oneplus6t.txt","w", encoding="utf-8") as output:
    for i in oneplus_reviews:
        output.write(i+"\n")
    
import os
os.getcwd()

#joining all the reviews into single paragraph/string
#data cleansing
op_rev_string = " ".join(oneplus_reviews)

#removing unwanted symbols if exists

op_rev_string = re.sub("[^A-Za-z" "]+"," ", op_rev_string).lower()
op_rev_string = re.sub("[0-9" "]+"," ",op_rev_string)

#tokenization : split the words from paragraph
op_reviews_words = op_rev_string.split(" ")

#stopwords
with open("D:/ExcelR/By ExcelR/Stopwords.txt") as sw:
    stopwords=sw.read()
stopwords = stopwords.split("\n")
stopwords.extend(["oneplus","camera","phone","amazon","time","headphone"])

op_reviews_words1 = [w for w in op_reviews_words if not w in stopwords]
op_rev_string1= " ".join(op_reviews_words1)

#wordcloud
wordcloud_op = WordCloud(
                    background_color= "white",
                    width = 1800,
                    height = 1400
                    ).generate(op_rev_string1)

plt.imshow(wordcloud_op)

#positive words
with open("D:/ExcelR/By ExcelR/positive-stopwords.txt") as pos:
    poswords=pos.read()
poswords = poswords.split("\n")

op_review_pos=" ".join([w for w in op_reviews_words if w in poswords])
wordcloud_pos = WordCloud(
                    background_color= "white",
                    width=1800,
                    height=1400).generate(op_review_pos)
plt.figure(2)
plt.imshow(wordcloud_pos)

 










