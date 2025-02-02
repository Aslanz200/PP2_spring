movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


#1
def rating(a):
    for i in movies:
        if a == i["name"] and i["imdb"]>5.5:
            return True
    return False



#2
def sublist(movies):
    result = []
    for i in movies:
        if i["imdb"] > 5.5:
            result.append(i["name"])
    return result


#3
def category(a):
    result = []
    for i in movies:
        if a == i["category"]:
            result.append(i["name"])
    return result


#4
def average(a):
    count = len(a)
    sum = 0
    for j in movies:
        for i in a:
            if i == j["name"]:
                sum += j["imdb"]
    aver = sum/count
    return aver



#5
def average_category(a):
    count = 0
    sum = 0
    for i in movies:
        if a == i["category"]:
            count += 1
            sum += i["imdb"]
    aver = sum/count
    return aver



