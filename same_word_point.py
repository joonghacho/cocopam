import re

def get_score(my_word, word):
    score = 0
    for cancan in my_word:
        if cancan == word:
            score += 1
    return score

def get_last_score(my_links, external_links, scores, last_scores):
    last_scores = []
    link_score = []
    for i in range(len(external_links)):
        ls = scores[i] / len(external_links[i])
        link_score.append(ls)
    for mine_i in range(len(my_links)):
        last_s = 0
        last_s += scores[mine_i]
        for ext_i in range(len(external_links)):
            if my_links[mine_i] in external_links[ext_i]:
                last_s += link_score[ext_i]
        last_scores.append(last_s)
    return last_scores

def get_body(page):
    body_parent = re.split('<body>|</body>', page)
    return body_parent[1]

def get_words(body):
    word_body = re.split('<a href|</a>', body)
    word_candi = []
    for candidate in word_body:
        if candidate[0] != "=":
            word_candi.append(candidate)
    # print("word_candi:", word_candi)
    answer_word = []
    for w in word_candi:
        low_w = w.lower()
        answer_candi = re.split('\W', low_w)
        answer_word += answer_candi
    # print(answer_word, "ddddfdsfasfasdfasdf")
    real_answer_word = []
    for ww in answer_word:
        real_candi = re.split('\d', ww)
        real_answer_word += real_candi
    # print(real_answer_word,"dfsdafasdfasgsagasg")
    wow_answer = []
    for aa in real_answer_word:
        if aa != "":
            wow_answer.append(aa)
    return wow_answer

def get_links(body):
    link_body = re.split('<a href|</a>', body)
    link_candi = []
    for candidate in link_body:
        if candidate[0] == "=":
            link_candi.append(candidate)
    link_answer = []
    for real_link in link_candi:
        pre_real_link = re.split('"', real_link)
        link_answer.append(pre_real_link[1])
    return link_answer

def get_my_link(page):
    new_pages = re.split('content|/>', page)
    my_candi = new_pages[1]
    new_my_candi = re.split('"', my_candi)
    return new_my_candi[1]


# def solution(word, pages):
#     answer = 0
#     return answer


pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]

new_pages = re.split('content=|<a href=|<body>|</body>|Link to|</head> ', pages[0])



if __name__ == "__main__":
    # print("sex",new_pages[1])
    # print("sex",new_pages[2])
    # print("sex",new_pages[3])

    # page_1_body = get_body(pages[0])
    # print(page_1_body)
    #
    # one_links = get_links(page_1_body)
    # print(one_links)
    #
    # my_link = get_my_link(pages[1])
    # print(my_link)
    #
    # one_body = get_words(page_1_body)
    # # print("sex!!!!!!!!!!")
    # print(one_body)
    word = "blind"
    my_links = []
    external_links = []
    my_words = []
    scores = []
    last_scores = []
    for each_page in pages:
        ma = get_my_link(each_page)
        my_links.append(ma)
        each_body = get_body(each_page)
        ext = get_links(each_body)
        external_links.append(ext)
        my_word = get_words(each_body)
        my_words.append(my_word)
    for cang in my_words:
        each_score = get_score(cang, word)
        scores.append(each_score)

    print(my_links)
    print(external_links)
    print(my_words)
    print(scores)

    answer = get_last_score(my_links, external_links, scores, last_scores)
    # print(answer)

    maxi = max(answer)
    for iii in range(len(answer)):
        if answer[iii] == maxi:
            real_real_answer = iii

    print(real_real_answer)