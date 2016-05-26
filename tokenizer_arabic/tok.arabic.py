

import re
import nltk

lex = u" في_بيتنا كل شي لما تحتاجه يضيع ...ادور على شاحن فجأة يختفي ..لدرجة اني اسوي نفسي ادور شيء"

wordsArray = nltk.tokenize.wordpunct_tokenize(lex)
print wordsArray