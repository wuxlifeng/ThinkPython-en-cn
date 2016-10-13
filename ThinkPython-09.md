Title: ThinkPython 双语学编程 Chapter 9
Date: 2015-11-30
Category: ThinkPython
Tag: 双语,Python,ThinkPython

#Chapter 9  Case study: word play 
>## 案例学习：单词游戏

This chapter presents the second case study, which involves solving word puzzles by searching for words that have certain properties. For example, we’ll find the longest palindromes in English and search for words whose letters appear in alphabetical order. And I will present another program development plan: reduction to a previously-solved problem.
>本章我们进行第二个案例学习，这一案例中涉及到了用搜索具有某些特征的单词来猜谜。比如，我们会发现英语中最长的回文词，然后搜索那些按照单词表顺序排列字母的单词。我还会给出一种新的程序开发计划：降低问题的复杂性和难度，还原到以前解决的问题。

##9.1  Reading word lists 读取字符列表

For the exercises in this chapter we need a list of English words. There are lots of word lists available on the Web, but the one most suitable for our purpose is one of the word lists collected and contributed to the public domain by Grady Ward as part of the Moby lexicon project (see [Here](http://wikipedia.org/wiki/Moby_Project)). It is a list of 113,809 official crosswords; that is, words that are considered valid in crossword puzzles and other word games. In the Moby collection, the filename is 113809of.fic; you can download a copy, with the simpler name words.txt, from [Here](http://thinkpython2.com/code/words.txt).
>本章练习中，咱们需要用一个英语词汇列表。网上有很多，不过最适合我们的列表并且是共有领域的，莫过于 Grady Ward 这份词汇表，这是 Moby 词典计划的一部分（点击[此链接访问详情](http://wikipedia.org/wiki/Moby_Project)）。这是一份 113，809 个公认的字谜表；也就是公认可以用于字谜游戏以及其他文字游戏的单词。在 Moby 的词汇项目中，该词表的文件名为 113809of.fic；你可以下载一份副本，这里名字简化成 words.txt 了，下载地址[在这里](http://thinkpython2.com/code/words.txt)。



This file is in plain text, so you can open it with a text editor, but you can also read it from Python. The built-in function open takes the name of the file as a parameter and returns a file object you can use to read the file.
>这个文件就是纯文本，所以你可以用文本编辑器打开一下，不过也可以用 Python 来读取。Python 内置了一个叫 open 的函数，接收文件名做参数，返回一个文件对象，你可以用它来读取文件。


```Python
>>> fin = open('words.txt')
```


fin is a common name for a file object used for input. The file object provides several methods for reading, including readline, which reads characters from the file until it gets to a newline and returns the result as a string:
>fin 是一个用来表示输入的文件的常用名字。这个文件对象提供了好几种读取的方法，包括逐行读取，这种方法是读取文本中的一整行直到结尾，然后把读取的内容作为字符串返回：


```Python
>>> fin.readline()
'aa\r\n'
```



The first word in this particular list is “aa”, which is a kind of lava. The sequence \r\n represents two whitespace characters, a carriage return and a newline, that separate this word from the next.
The file object keeps track of where it is in the file, so if you call readline again, you get the next word:
>这一列当中的第一个词就是『aa』了，这是一种**熔岩**（译者注：“aa” 是夏威夷词汇，音“阿阿”，用来描述表面粗糙的熔岩流。译者本人就是地学专业的，都很少接触这个词，本教材作者真博学啊）。后面跟着的 \r\n 的意思代表着有两个转义字符，一个是回车，一个是换行，这样把这个单词从下一个单词分隔开来。
>文件对象会记录这个单词在源文件中的位置，所以下次你再调用 readline 的时候，就能得到下一个词了：



```Python
>>> fin.readline()
'aah\r\n'
```


The next word is “aah”, which is a perfectly legitimate word, so stop looking at me like that. Or, if it’s the whitespace that’s bothering you, we can get rid of it with the string method strip:
>下一个词是『aah』，这完全是一个正规的词汇，不要怪异眼神看我哦。另外如果转义字符让你很烦，咱们可以稍加修改来去掉它，用字符串的 strip 方法即可：

```Python
>>> line = fin.readline()
>>> word = line.strip()
>>> word
'aahed'
```


You can also use a file object as part of a for loop. This program reads words.txt and prints each word, one per line:
>在 for 循环中也可以使用文件对象。下面的这个程序读取整个 words.txt 文件，然后每行输出一个词：

```Python
fin = open('words.txt')
	for line in fin:
		word = line.strip()
		print(word)
```


##9.2  Exercises 练习
There are solutions to these exercises in the next section. You should at least attempt each one before you read the solutions.
>下面这些练习都有样例代码。不过你最好在看答案之前先自己对每个练习都尝试一下。


###Exercise 1 练习1
Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace).
>写一个程序读取 words.txt，然后只输出超过 20 个字母长度的词（这个长度不包括转义字符）。

###Exercise 2 练习2

In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter “e”. Since “e” is the most common letter in English, that’s not easy to do.
>在 1939 年，作家厄尔尼斯特·文森特·莱特曾经写过一篇 5 万字的小说《葛士比》，里面没有一个字母 e。因为在英语中 e 是用的次数最多的字母，所以这很不容易的。

In fact, it is difficult to construct a solitary thought without using that most common symbol. It is slow going at first, but with caution and hours of training you can gradually gain facility.
>事实上，不使用最常见的字符，都很难想出一个简单的想法。一开始很慢，不过仔细一些，经过几个小时的训练之后，你就逐渐能做到了。

All right, I’ll stop now.
Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.
>好了，我不扯淡了。
>写一个名字叫做 has_no_e 的函数，如果给定词汇不含有 e 就返回真，否则为假。

Modify your program from the previous section to print only the words that have no “e” and compute the percentage of the words in the list that have no “e”.
>修改一下上一节的程序代码，让它只打印单词表中没有 e 的词汇，并且统计一下这些词汇在总数中的百分比例。


###Exercise 3 练习3
Write a function named avoids that takes a word and a string of forbidden letters, and that returns True if the word doesn’t use any of the forbidden letters.
Modify your program to prompt the user to enter a string of forbidden letters and then print the number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters that excludes the smallest number of words?
>写一个名叫 avoids 的函数，接收一个单词和一个禁用字母组合的字符串，如果单词不含有该字符串中的任何字母，就返回真。
>修改一下程序代码，提示用户输入一个禁用字母组合的字符串，然后输入不含有这些字母的单词数目。你能找到5个被禁用字母组合，排除单词数最少吗？



###Exercise 4 练习4
Write a function named uses_only that takes a word and a string of letters, and that returns True if the word contains only letters in the list. Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa”?
>写一个名叫 uses_only 的函数，接收一个单词和一个字母字符串，如果单词仅包含该字符串中的字母，就返回真。你能仅仅用 acefhlo 这几个字母造句子么？或者试试『Hoe alfalfa』?

###Exercise 5 练习5
Write a function named uses_all that takes a word and a string of required letters, and that returns True if the word uses all the required letters at least once. How many words are there that use all the vowels aeiou? How about aeiouy?
>写一个名字叫 uses_all 的函数，接收一个单词和一个必需字母组合的字符串，如果单词对必需字母组合中的字母至少都用了一次就返回真。有多少单词都用到了所有的元音字母 aeiou？aeiouy 的呢？



###Exercise 6 练习6
Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok). How many abecedarian words are there?
>写一个名字叫 is_abecedarian 的函数，如果单词中所有字母都是按照字母表顺序出现就返回真（重叠字母也是允许的）。有多少这样的单词？




##9.3  Search 搜索
All of the exercises in the previous section have something in common; they can be solved with the search pattern we saw in Section 8.6. The simplest example is:
>刚刚的那些练习都有一些相似之处：都可以用我们在 [8.6](ThinkPython-08.md#86--searching-搜索) 学过的搜索来解决。下面是一个最简化的例子：

```Python
def has_no_e(word):
	for letter in word:
		if letter == 'e':
			return False
	return True
```



The for loop traverses the characters in word. If we find the letter “e”, we can immediately return False; otherwise we have to go to the next letter. If we exit the loop normally, that means we didn’t find an “e”, so we return True.
>这个 for 循环遍历了单词的所有字母。如果找到了字母 e，就立即返回假；否则就到下一个字母。如果正常退出了循环，意味着我们没找到 e，就返回真。


You could write this function more concisely using the in operator, but I started with this version because it demonstrates the logic of the search pattern.
avoids is a more general version of has_no_e but it has the same structure:
>你可以使用 in 运算符，把这个函数写得更精简，我之所以用一个稍显麻烦的版本，是为了说明搜索模式的逻辑过程。
>avoids 是一个更通用版本的 has_no_e 函数的实现，它的结构是一样的：

```Python
def avoids(word, forbidden):
	for letter in word:
		if letter in forbidden:
			return False
	return True
```

We can return False as soon as we find a forbidden letter; if we get to the end of the loop, we return True.
uses_only is similar except that the sense of the condition is reversed:
>只要找到了禁用字母就可以立即返回假；如果运行到了循环末尾，就返回真。
>uses_only 与之相似，无非是条件与之相反了而已。

```Python
def uses_only(word, available):
	for letter in word:
		if letter not in available:
			return False
	return True
```


Instead of a list of forbidden letters, we have a list of available letters. If we find a letter in word that is not in available, we can return False.
uses_all is similar except that we reverse the role of the word and the string of letters:
>这次不是有一个禁用字母列表，我们这次用一个可用字母列表。如果在单词中发现不在可用字母列表中的，就返回假了。
>uses_all 这个函数与之也相似，不过我们转换了单词和字母字符串的角色：

```Python
def uses_all(word, required):
	for letter in required:
		if letter not in word:
			return False
	return True
```



Instead of traversing the letters in word, the loop traverses the required letters. If any of the required letters do not appear in the word, we can return False.
If you were really thinking like a computer scientist, you would have recognized that uses_all was an instance of a previously-solved problem, and you would have written:
>这次并没有遍历单词中的所有字母，循环遍历了所有指定的字母。如果有任何指定字母没有在单词中出新啊，就返回假。如果你已经像计算机科学家一样思考了，你就应该已经发现了 uses_all 是对之前我们解决过问题的一个实例，你已经写过这个代码了：

```Python
def uses_all(word, required):
	return uses_only(required, word)
```


This is an example of a program development plan called reduction to a previously-solved problem, which means that you recognize the problem you are working on as an instance of a solved problem and apply an existing solution.
>这就是一种新的程序开发规划模式，就是降低问题的复杂性和难度，还原到以前解决的问题，意思是你发现正在面对的问题是之前解决过的问题的一个实例，就可以用已经存在的方案来解决。




##9.4  Looping with indices 带索引循环

I wrote the functions in the previous section with for loops because I only needed the characters in the strings; I didn’t have to do anything with the indices.
For is_abecedarian we have to compare adjacent letters, which is a little tricky with a for loop:
>上面的章节中我写了各种用 for 循环的函数，因为当时只需要字符串中的字符；这就不需要理会索引。
>但 is_abecedarian 这个函数中，我们需要对比临近的两个字母，所以用 for 循环就不那么好写了：

```Python
def is_abecedarian(word):
	previous = word[0]
	for c in word:
		if c < previous:
			return False
		previous = c
	return True
```


An alternative is to use recursion:
>一种很好的替代思路就是使用递归：


```Python
def is_abecedarian(word):
	if len(word) <= 1:
		return True
	if word[0] > word[1]:
		return False
	return is_abecedarian(word[1:])
```


Another option is to use a while loop:
>另外一种方法是用 while 循环：

```Python
def is_abecedarian(word):
	i = 0
	while i < len(word)-1:
		if word[i+1] < word[i]:
		return False
		i = i+1
	return True
```

The loop starts at i=0 and ends when i=len(word)-1. Each time through the loop, it compares the ith character (which you can think of as the current character) to the i+1th character (which you can think of as the next).
>循环开始于 i 等于 0，然后在 i 等于 len(word)-1 的时候结束。每次通过循环的时候，都对比第 i 个字符（你可以就当是当前字符）与第 i+1 个字符（就当作下一个字符）。

If the next character is less than (alphabetically before) the current one, then we have discovered a break in the abecedarian trend, and we return False.
>如果下一个字符比当前字符小（字母表排列顺序在当前字符前面），我们就发现这个不符合字母表顺序了，跳出返回假就可以了。

If we get to the end of the loop without finding a fault, then the word passes the test. To convince yourself that the loop ends correctly, consider an example like 'flossy'. The length of the word is 6, so the last time the loop runs is when i is 4, which is the index of the second-to-last character. On the last iteration, it compares the second-to-last character to the last, which is what we want.
>如果一直到循环结尾都没有发现问题，这个词就通过检验了。为了确信循环正确结束了，可以拿单词『flossy』作为例子来试试。单词长度是 6，所以循环终止的时候 i 应该是 4，也就是倒数第二个位置。在最后一次循环中，比较的是倒数第二个和最后一个字母，这正是符合我们设计的。

Here is a version of is_palindrome (see Exercise 3) that uses two indices; one starts at the beginning and goes up; the other starts at the end and goes down.
>下面这个是练习 3 的 is_palindrome 的一个版本，使用了两个索引；一个从头开始一直到结尾；另外一个从末尾开始逆序进行。

```Python
def is_palindrome(word):
	i = 0
	j = len(word)-1
	while i<j:
		if word[i] != word[j]:
			return False
		i = i+1
		j = j-1
	return True
```



Or we could reduce to a previously-solved problem and write:
>或者我们可以把问题解构成之前解决过的样式，然后这样写：

```Python
def is_palindrome(word):
	return is_reverse(word, word)
```

Using is_reverse from Section 8.11.
>这里的 is_reverse 这个函数在 [8.11](ThinkPython-08.md#811--debugging-调试) 节讲过哈。



##9.5  Debugging 调试

Testing programs is hard. The functions in this chapter are relatively easy to test because you can check the results by hand. Even so, it is somewhere between difficult and impossible to choose a set of words that test for all possible errors.
>测试程序很难的。本章的函数相对来说还算容易测试，因为你可以手动计算来检验结果。即便如此，选择一系列单词然后检测所有可能的错误，可能不仅是做起来困难，甚至都是不可能完成的任务。


Taking has_no_e as an example, there are two obvious cases to check: words that have an ‘e’ should return False, and words that don’t should return True. You should have no trouble coming up with one of each.
>比如以 has_no_e 为例，有两种情况用来检查：有 e 的单词应该返回假，不包含 e 的单词要返回真。你自己想出几个这样的单词来检验一下并不难。


Within each case, there are some less obvious subcases. Among the words that have an “e”, you should test words with an “e” at the beginning, the end, and somewhere in the middle. You should test long words, short words, and very short words, like the empty string. The empty string is an example of a special case, which is one of the non-obvious cases where errors often lurk.
>在每个分支内，有一些不那么清晰的次级分支。在那些有 e 的单词中，你还要检测单词中的 e 是在开头结尾还是中间位置。你得试试长词、短词，甚至特别短的词，比如空字符串。空字符串是一个典型特例，这个情况很容易被忽视而成为潜伏的隐患。
>（译者注：我知道，这段翻译的简直就是 shit，但是没办法，我这会眼睛特别疼，思路不太清楚，另外这几个练习也不是很难，大家很容易自己搞定。）


In addition to the test cases you generate, you can also test your program with a word list like words.txt. By scanning the output, you might be able to catch errors, but be careful: you might catch one kind of error (words that should not be included, but are) and not another (words that should be included, but aren’t).
>除了你自己设计的测试案例之外，你也可以用一个单词列表比如 words.txt 之类的来测试一下你的程序。通过扫描一下输出内容，你也许能够发现错误的地方，但一定要小心：你有可能发现某一种特定错误，但忽略了另外一个，比如包含了不应该包含的单词，但很难发现应该包含但遗漏了单词的情况。

In general, testing can help you find bugs, but it is not easy to generate a good set of test cases, and even if you do, you can’t be sure your program is correct. According to a legendary computer scientist:
Program testing can be used to show the presence of bugs, but never to show their absence!
— Edsger W. Dijkstra
>总的来说，测试程序能帮助你找到错误地方，但很难找到一系列特别好的测试案例，或者即便你找了很多案例来测试，也不能确保程序就是正确的。一位传说级别的计算机科学家说：
>程序测试可以用来表明 bug 的存在，但永远不能表明 bug 不存在。
>— Edsger W. Dijkstra


##9.6  Glossary 术语列表

file object:
A value that represents an open file.
>文件对象：代表了一份打开的文件的值。

reduction to a previously-solved problem:
A way of solving a problem by expressing it as an instance of a previously-solved problem.
>降低问题的复杂性和难度，还原到以前解决的问题：一种解决问题的方法，把问题表达成过去解决过问题的一个特例。

special case:
A test case that is a typical or non-obvious (and less likely to be handled correctly).
>特殊案例：很典型或者不明显的测试用的案例，往往都很不容易正确处理。



##9.7  Exercises 练习

###Exercise 7 练习7
[This question](http://www.cartalk.com/content/puzzlers)is based on a Puzzler that was broadcast on the radio program Car Talk :
Give me a word with three consecutive double letters. I’ll give you a couple of words that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could take out those i’s it would work. But there is a word that has three consecutive pairs of letters and to the best of my knowledge this may be the only word. Of course there are probably 500 more but I can only think of one. What is the word?
Write a program to find it.
[Solution](http://thinkpython2.com/code/cartalk1.py)
>[这个问题](http://www.cartalk.com/content/puzzlers)基于一个谜语，这个谜语在广播节目 Car Talk 上面播放过：
>给我一个有三个连续双字母的单词。我会给你一对基本符合的单词，但并不符合。例如， committee 这个单词，C O M M I T E。如果不是有单独的一个 i 在里面，就基本完美了，或者 Mississippi 这个词：M I S I S I P I。如果把这些个 i 都去掉就好了。但有一个词正好是三个重叠字母，而且据我所知这个词可能是唯一一个这样的词。当然有有可能这种单词有五百多个呢，但我只能想到一个。是哪个词呢？写个程序来找一下这个词吧。
>[样例代码](http://thinkpython2.com/code/cartalk1.py)



###Exercise 8 练习8
[Here](http://www.cartalk.com/content/puzzlers)’s another Car Talk Puzzler :
“I was driving on the highway the other day and I happened to notice my odometer. Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000 miles, for example, I’d see 3-0-0-0-0-0.
“Now, what I saw that day was very interesting. I noticed that the last 4 digits were palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a palindrome, so my odometer could have read 3-1-5-4-4-5.
“One mile later, the last 5 numbers were palindromic. For example, it could have read 3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And you ready for this? One mile later, all 6 were palindromic!
“The question is, what was on the odometer when I first looked?”
Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy these requirements. [Solution](http://thinkpython2.com/code/cartalk2.py)
>[这个](http://www.cartalk.com/content/puzzlers)又是一个 Car Talk 谜语：
>有一天我在高速路上开着车，碰巧看了眼里程表。和大多数里程表一样，是六位数字的，单位是英里。加入我的车跑过 300，000 英里了，看到的结果就是 3-0-0-0-0-0.
>我那天看到的很有趣，我看到后四位是回文的；就是说后四位正序和逆序读是一样的。例如 5-4-4-5 就是一个回文数，所以我的里程表可能读书就是 3-1-5-4-4-5.
>过了一英里之后，后五位数字是回文的了。举个例子，可能读书就是 3-6-5-4-5-6。又过了一英里，六个数字中间的数字是回文数了。准备好更复杂的了么？又过了一英里，整个六位数都是回文的了！
>那么问题俩了：我最开始看到的里程表的度数应该是多少？
>写个 Python 程序来检测一下所有的六位数，然后输出一下满足这些要求的数字。 [样例代码](http://thinkpython2.com/code/cartalk2.py)



###Exercise 9 练习9
[Here](http://www.cartalk.com/content/puzzlers)’s another Car Talk Puzzler you can solve with a search :
“Recently I had a visit with my mom and we realized that the two digits that make up my age when reversed resulted in her age. For example, if she’s 73, I’m 37. We wondered how often this has happened over the years but we got sidetracked with other topics and we never came up with an answer.
“When I got home I figured out that the digits of our ages have been reversible six times so far. I also figured out that if we’re lucky it would happen again in a few years, and if we’re really lucky it would happen one more time after that. In other words, it would have happened 8 times over all. So the question is, how old am I now?”
Write a Python program that searches for solutions to this Puzzler. Hint: you might find the string method zfill useful.
[Solution](http://thinkpython2.com/code/cartalk3.py)
>[这个](http://www.cartalk.com/content/puzzlers)又是一个 Car Talk 谜语，你可以用搜索来解决：
>最近我看忘了妈妈，然后我们发现我的年龄反过来正好是她的年龄。例如，假如他是 73 岁，我就是 37 岁了。我们好奇这种情况发生多少次，但中间叉开了话题，没有想出来这个问题的答案。
>我回家之后，我发现到目前位置我们的年龄互为逆序已经是六次了，我还发现如果我们幸运的话过几年又会有一次，如果我们特别幸运，就还会再有一次这样情况。换句话说，就是总共能有八次。那么问题来了：我现在多大了？
>写一个 Python 程序，搜索一下这个谜语的解。提示一下：你可能发现字符串的 zfill 方法很有用哦。
>[样例代码](http://thinkpython2.com/code/cartalk3.py)

[Chapter 8](ThinkPython-08.md) | [Chapter 10](ThinkPython-10.md)
