from django.shortcuts import render

from django.http import HttpResponse
import pandas as pd
import json
import pymysql

# Create your views here.
# 从数据库中导入数据
conn = pymysql.connect(host="127.0.0.1", user="root", password="root", db="movie")
movies_df1 = pd.read_sql("select * from movie_metadata", conn)
# 从csv文件中导入数据
movies_df = pd.read_csv("E:\coding\python\movie\movie_metadata.csv")

# 数据清洗——去重
movies_df = movies_df.drop_duplicates()
# 数据清洗——处理缺失值
movies_df = movies_df.dropna()  # 默认丢失任何含有缺失值的行，滤除缺失数据，仅含非空数据，传入参数‘how='all’将只丢弃那些全为NA的行，要丢弃列只需传入axis=1即可。
# or
# movies_df = movies_df.fillna(movies_df['duration'].mean())  # 填充缺失数据

# 电影出品数量排名前10位的国家
def test1(request):

    # 电影出品数量排名前10位的国家及地区
    grouped = movies_df.groupby('country').size()
    grouped_head_10 = grouped.sort_values(ascending=False).head(10)

    res = {}
    list1 = []
    list2 = []

    for key, value in grouped_head_10.items():
        list1.append(key)
        list2.append(value)
        print(key, value)
    res['list1'] = list1
    res['list2'] = list2

    return HttpResponse(json.dumps(res), content_type='application/json; charset=UTF-8')

# imdb 评分前十电影
def test2(request):

    # imdb 评分前十电影

    movie_max1 = movies_df.sort_values(['imdb_score'], ascending=False).head(15)
    movie_max2 = pd.Series(movie_max1['imdb_score'].values, index=movie_max1['movie_title'])

    res = {}
    list1 = []
    list2 = []

    for key, value in movie_max2.items():
        list1.append(key)
        list2.append(value)
        print(key, value)
    res['list1'] = list1
    res['list2'] = list2

    return HttpResponse(json.dumps(res), content_type='application/json; charset=UTF-8')

# 票房前十电影
def test3(request):
    # 票房前十电影
    movies_max = movies_df.sort_values(['gross'], ascending=False).head(10)
    movie_max4 = pd.Series(movies_max['gross'].values, index=movies_max['movie_title'])

    res = {}
    list1 = []
    list2 = []
    for key, value in movie_max4.items():
        list1.append(key)
        list2.append(value)
        print(key, value)

    res['list1'] = list1
    res['list2'] = list2

    return HttpResponse(json.dumps(res), content_type='application/json; charset=UTF-8')

# 每年上映电影
def test4(request):
    # 每年上映电影数量
    grouped_year_title = movies_df.groupby('title_year')['movie_title'].count()

    # 每年上映电影总票房
    movies_year_gross = movies_df.groupby(['title_year'])['gross'].sum()

    # 每年上映电影总成本
    movies_year_budget = movies_df.groupby(['title_year'])['budget'].sum()

    # 每年上映电影总利润
    movies_year = movies_df.groupby(['title_year'])['gross', 'budget'].sum()
    profit = movies_year['gross'] - movies_year['budget']

    res = {}
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []

    for key, value1 in grouped_year_title.items():
        list1.append(key)
        list2.append(value1)
        print(key, value1)
    for key, value2 in movies_year_gross.items():
        list3.append(value2)
        print(value2)
    for key, value3 in movies_year_budget.items():
        list4.append(value3)
        print(value3)
    for key, value4 in profit.items():
        list5.append(value4)
        print(value4)
    res['list1'] = list1
    res['list2'] = list2
    res['list3'] = list3
    res['list4'] = list4
    res['list5'] = list5

    return HttpResponse(json.dumps(res), content_type='application/json; charset=UTF-8')

# 不同色彩电影数量
def test5(request):

    # 每年电影总数量
    num1 = movies_df.groupby('title_year')['movie_title'].count()
    # 黑白影片数量
    num2 = movies_df[movies_df['color'] != 'Color']['title_year'].value_counts().sort_index()
    # 彩色影片数量
    num3 = movies_df[movies_df['color'] == 'Color']['title_year'].value_counts().sort_index()


    res = [[], [], [], []]
    list1 = ['product']
    list2 = ['电影总数量']
    list3 = ['黑白电影']
    list4 = ['彩色电影']

    for key, value1 in num1.items():
        list1.append(key)
        list2.append(value1)

    tmp = len(num1) - len(num2)
    for i in range(tmp):
        list3.append(0)
    for key, value2 in num2.items():
        list3.append(value2)

    tmp = len(num1) - len(num3)
    for i in range(tmp):
        list4.append(0)
    for key, value3 in num3.items():
        list4.append(value3)

    res[0].extend(list1)
    res[1].extend(list2)
    res[2].extend(list3)
    res[3].extend(list4)

    return HttpResponse(json.dumps(res), content_type='application/json; charset=UTF-8')

# 不同类型电影数量
def test6(request):

    # 创建字典用于存储电影类型
    types = []
    for tp in movies_df['genres']:
        sp = tp.split('|')
        for x in sp:
            types.append(x)
    # 格式化
    types_df = pd.DataFrame({'genres': types})
    types_df_counts = types_df['genres'].value_counts()
    print(types_df_counts.head(10))

    res = {}
    list1 = []
    list2 = []

    for key, value1 in types_df_counts.items():
        list1.append(key)
        list2.append(value1)
        print(key, value1)
    res['list1'] = list1
    res['list2'] = list2

    return HttpResponse(json.dumps(res), content_type='application/json; charset=UTF-8')

# 票房前十喜欢人数
def test7(request):

    movies_max = movies_df.sort_values(['gross'], ascending=False).head(10)
    movies_max1 = movies_max[['actor_1_facebook_likes', 'actor_2_facebook_likes', 'actor_3_facebook_likes', 'cast_total_facebook_likes', 'director_facebook_likes', 'movie_facebook_likes']]
    df = pd.DataFrame({'喜爱演员1': movies_max1['actor_1_facebook_likes'].values,
                       '喜爱演员2': movies_max1['actor_2_facebook_likes'].values,
                       '喜爱演员3': movies_max1['actor_3_facebook_likes'].values,
                       '喜爱总演员': movies_max1['cast_total_facebook_likes'].values,
                       '喜爱导演': movies_max1['director_facebook_likes'].values,
                       '喜爱电影': movies_max1['movie_facebook_likes'].values},
                       index=movies_max['movie_title'].str.strip())

    res = {}
    set1 = []
    list1 = ["product", "喜爱演员1", "喜爱演员2", "喜爱演员3", "喜爱总演员", "喜爱导演", "喜爱电影"]

    for key, value in df.iterrows():
        tmp = {}
        tmp['product'] = key
        tmp['喜爱演员1'] = value['喜爱演员1']
        tmp['喜爱演员2'] = value['喜爱演员2']
        tmp['喜爱演员3'] = value['喜爱演员3']
        tmp['喜爱总演员'] = value['喜爱总演员']
        tmp['喜爱导演'] = value['喜爱导演']
        tmp['喜爱电影'] = value['喜爱电影']
        set1.append(tmp)

    res['set'] = set1
    res['list'] = list1

    return HttpResponse(json.dumps(res), content_type='application/json; charset=UTF-8')

# 相关性分析
def test8(request):

    cor = movies_df.corr()
    # cor1 = movies_df.corr()['gross']

    res = {}
    list1 = []
    list2 = []

    pos = 0
    max = 999
    for key, value in cor.items():
        list1.append(key)
        index = 0

        for k, v in value.items():
            if max > v:
                max = v
            tmp = []
            tmp.append(pos)
            tmp.append(index)
            tmp.append(v)
            list2.append(tmp)
            index += 1
        pos += 1

    res['list1'] = list1
    res['list2'] = list2

    return HttpResponse(json.dumps(res), content_type='application/json; charset=UTF-8')

# 每年上映电影imdb平均评分
def test9(request):
    # 每年上映电影imdb平均评分
    score_yr = movies_df.groupby(['title_year'])['imdb_score'].mean()
    print(score_yr)

    res = {}
    list1 = []
    list2 = []

    for key, value in score_yr.items():
        list1.append(key)
        list2.append(value)
        print(key, value)

    res['list1'] = list1
    res['list2'] = list2

    return HttpResponse(json.dumps(res), content_type='application/json; charset=UTF-8')

# 电影票房相关因素的分析
def test10(request):
    # 电影票房统计及电影票房相关因素的分析

    # 每年上映电影总票房
    movies_gross = movies_df['gross']
    # 电影时长
    movies_duration = movies_df['duration']
    # 电影评分
    movies_imdb_score = movies_df['imdb_score']
    # 投票用户数
    movies_budget = movies_df['num_voted_users']
    # 评论的用户数
    movies_facenumber_in_poster = movies_df['num_user_for_reviews']
    # 评论的评分数量
    movies_title_year = movies_df['num_critic_for_reviews']
    # 脸书喜欢人数
    movies_aspect_ratio = movies_df['movie_facebook_likes']


    res = {}
    list1 = [[] for i in range(len(movies_duration))]
    list2 = [[] for i in range(len(movies_imdb_score))]
    list3 = [[] for i in range(len(movies_budget))]
    list4 = [[] for i in range(len(movies_budget))]
    list5 = [[] for i in range(len(movies_budget))]
    list6 = [[] for i in range(len(movies_budget))]

    # print(len(grouped_year_title))
    pos = 0
    for i in movies_duration:
        list1[pos].append(i)
        pos += 1
    pos = 0
    for i in movies_gross:
        list1[pos].append(i)
        pos += 1


    pos = 0
    for i in movies_imdb_score:
        list2[pos].append(i)
        pos += 1
    pos = 0
    for i in movies_gross:
        list2[pos].append(i)
        pos += 1

    pos = 0
    for i in movies_budget:
        list3[pos].append(i)
        pos += 1
    pos = 0
    for i in movies_gross:
        list3[pos].append(i)
        pos += 1

    pos = 0
    for i in movies_facenumber_in_poster:
        list4[pos].append(i)
        pos += 1
    pos = 0
    for i in movies_gross:
        list4[pos].append(i)
        pos += 1

    pos = 0
    for i in movies_title_year:
        list5[pos].append(i)
        pos += 1
    pos = 0
    for i in movies_gross:
        list5[pos].append(i)
        pos += 1

    pos = 0
    for i in movies_aspect_ratio:
        list6[pos].append(i)
        pos += 1
    pos = 0
    for i in movies_gross:
        list6[pos].append(i)
        pos += 1

    res['list1'] = list1
    res['list2'] = list2
    res['list3'] = list3
    res['list4'] = list4
    res['list5'] = list5
    res['list6'] = list6

    return HttpResponse(json.dumps(res), content_type='application/json; charset=UTF-8')

# 电影脸书上受欢迎程度相关因素的分析
def test11(request):
    # 电影脸书上受欢迎程度相关因素的分析

    # 上映电影受欢迎人数
    movies_facebook_likes = movies_df['movie_facebook_likes']
    # 电影评分
    movies_imdb_score = movies_df['imdb_score']
    # 用户的评论数量
    movies_num_user_for_reviews = movies_df['num_user_for_reviews']
    # 参与投票的用户数量
    movies_num_voted_users = movies_df['num_voted_users']
    # 脸书上投喜爱的总数
    movies_cast_total_facebook_likes = movies_df['cast_total_facebook_likes']

    res = {}
    list1 = [[] for i in range(len(movies_imdb_score))]
    list2 = [[] for i in range(len(movies_num_user_for_reviews))]
    list3 = [[] for i in range(len(movies_num_voted_users))]
    list4 = [[] for i in range(len(movies_cast_total_facebook_likes))]

    # print(len(grouped_year_title))
    pos = 0
    for i in movies_imdb_score:
        list1[pos].append(i)
        pos += 1
    pos = 0
    for i in movies_facebook_likes:
        list1[pos].append(i)
        pos += 1

    pos = 0
    for i in movies_num_user_for_reviews:
        list2[pos].append(i)
        pos += 1
    pos = 0
    for i in movies_facebook_likes:
        list2[pos].append(i)
        pos += 1

    pos = 0
    for i in movies_num_voted_users:
        list3[pos].append(i)
        pos += 1
    pos = 0
    for i in movies_facebook_likes:
        list3[pos].append(i)
        pos += 1

    pos = 0
    for i in movies_cast_total_facebook_likes:
        list4[pos].append(i)
        pos += 1
    pos = 0
    for i in movies_facebook_likes:
        list4[pos].append(i)
        pos += 1

    res['list1'] = list1
    res['list2'] = list2
    res['list3'] = list3
    res['list4'] = list4

    return HttpResponse(json.dumps(res), content_type='application/json; charset=UTF-8')

# 脸书上排名前十的电影
def test12(request):
    # 脸书上排名前十的电影

    top_movies1 = movies_df.sort_values(['movie_facebook_likes'], ascending=False).head(15)
    top_movies = pd.Series(top_movies1['movie_facebook_likes'].values, index=top_movies1['movie_title'])


    res = {}
    list1 = []
    list2 = []

    for key, value in top_movies.items():
        list1.append(key)
        list2.append(value)
        print(key, value)

    res['list1'] = list1
    res['list2'] = list2

    return HttpResponse(json.dumps(res), content_type='application/json; charset=UTF-8')
