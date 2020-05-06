# 정규식의 lookahead, lookbehind 를 배운 아주 좋은 학습이었다.
# 두개를 통틀어 lookaround 라고 부르더라.
# 참고 사이트.
# https://www.regular-expressions.info/lookaround.html

import re


def getUrl(html):
    p = re.compile("<meta property=\"og:url\" content=\"(.*?)\"/>")
    m = p.search(html)
    return m.group(1)


def getLinks(html):
    p = re.compile("<a href=\"(.*?)\">")
    m = p.findall(html)
    return m


def matchWord(word, html):
    p = re.compile("(?<=[^a-z]){}(?![a-z])".format(word))
    m = p.findall(html)
    return len(m)


def solution(word, pages):
    n = len(pages)
    word = word.lower()

    urls = []
    links = []
    wordCnts = []
    for i in range(n):
        html = pages[i].lower()
        url = getUrl(html)
        urls.append(url)
        link = getLinks(html)
        links.append(link)
        wordMatch = matchWord(word, html)
        wordCnts.append(wordMatch)

    scores = []
    for i in range(n):
        baseScore = wordCnts[i]
        linkScore = 0
        for j in range(n):
            if j != i:
                if urls[i] in links[j]:
                    linkScore += wordCnts[j] / len(links[j])

        scores.append(baseScore + linkScore)

    maxi = max(scores)
    return scores.index(maxi)


word = 'Muzi'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
         "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

print(solution(word, pages))
