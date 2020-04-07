# readFIB
Erm...我是有多不想学PTE哦...

Well, I write another tool to **'help'** me to learn PTE since the [crawler](https://github.com/rainshang/60sScienceCrawler).

It is a python3 script this time, to practise word dictation.

Basically just run it and it will read the `FIB.md` file in parent directory by default. Also, I allow you to input the file as the argument.

![](img/0.png)

The `FIB.md` should be like this,

![](img/1.png)

all the non-word lines like the `<span>` will be ignored.

Then press `Enter` to begin your dictation. *Notice:* Recommend to enter your answer after the `Your answer: ` shows. I know it's slow, limited by the text-to-speech lib though.

![](img/2.png)

Moreover, it supports only reviewing the words you haven't mastered using the option `-o`, and the words are identified by tag `<meijizhu>`.

![](img/3.png)

I also provide the option `-s` to specify the starting line. Use `-h` or `--help` to see the detail.

Again, enjoy and have fcking good luck!