import bs4

print(dir(bs4))

# def square(nums):
#     for i in nums:
#         yield i**2

# nums = square([1,2,3,4,5,6,7])
# for c in nums:
#     print(c)

# print(next(nums))
# lst = [1,2,3,4,5,6,7]
# lst = range(10)
# nums = (i**2 for i in lst)
# for c in nums:
#     print(c)
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))












# def iterator(low,high):
#     curr=low
#     while curr <= high:
#         yield curr
#         curr +=1

# for c in iterator(3,8):
#     print(c)

# class iterator:
#     def __init__(self,min,max):
#         self.curr = min
#         self.high = max

#     def __iter__(self):
#         return self

#     def next(self):
#         if self.curr<self.high:
#             self.curr +=1
#             return self.curr-1
#         else:
#             raise StopIteration()

# for c in iterator(3,8):
#     print(c)


# for i in range(20):
#     print('FizzBuzz' if i%5==0 and i%3==0
#         else 'Fizz' if i%5==0
#         else 'Buzz' if i%3==0
#         else i)
# import json
# from urllib.request import urlopen

# with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as r:
#     # print(r)
#     src = r.read()
#     print(src)

# # data = json.loads(src)
# # # print(json.dumps(data,indent =2))
# # usd_rates = {}

# # for item in data["list"]["resources"]:
# #     # print(item)
# #     name = item['resource']['fields']['name']
# #     price = item['resource']['fields']['price']

# #     usd_rates[name] = price

# # print(50 * float(usd_rates['USD/INR']))
