import re


def getUrl(html):
    p = re.compile("<meta property=\"og:url\" content=\"(https://[a-z.@]*?)\"/>")
    m = p.search(html)
    print(m.group())
    return m.group()


def getLinks(html):
    p = re.compile("<a href=\"(https://[a-z.@]*?)\">")
    m = p.findall(html)
    return m


def matchWord(word, html):
    p = re.compile("[^a-z]{}[^a-z]".format(word))
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
        # print(link)
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


# 기본점수: 검색어 등장횟수
# 외부링크 수: 다른 외부 페이지로 연결된 링크 개수
# 링크점수: 이 웹페이지로 링크가 걸린 다른 웹페이지들의 (기본 점수 / 외부링크 수) 총합
# 매칭점수: 기본점수 + 링크점수
word = 'Muzi'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
         "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

print(solution(word, pages))
