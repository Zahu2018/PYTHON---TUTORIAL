HEADERS
# H1
## H2
### H3
#### H4
##### H5
###### H6

Alt-H1
======

Alt-H2
------

EMPHASIS

*italic*, _italic_
**bold**, __bold__
~strike~

LISTS - ordered

1. First item
2. Second items

LISTS - unordered

* First item
* Second item
+ Third item
- Fourth item

LISTS - sub-list

1. First item
--1. Sublist
--* Sublist item 

* Unordered list can use asterisks
- Or minuses
+ Or pluses

TABLES

| Syntax       | Description | Test Text     |
| :---         |    :----:   |          ---: |
| Header       | Title       | Here's this   |
| Left align   | Center      | Right align   |

CODE & HIGHLIGHT SYNTAX

`print(f)`

```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

FOOTNOTES

[^1]: This is the first footnote.

TASK LIST

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

LINKS

[link](https://www.google.com)

[link with title](https://www.google.com "Google's Homepage")

[link reference-style][Arbitrary case-insensitive reference text]

[link to a repository file](../blob/master/LICENSE)

[link reference-style definitions][1]

URLs and URLs in angle brackets will automatically get turned into links. 
http://www.example.com or <http://www.example.com> and sometimes 
example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com
I'm an inline-style link

I'm an inline-style link with title

I'm a reference-style link

I'm a relative reference to a repository file

You can use numbers for reference-style link definitions

Or leave it empty and use the link text itself.

URLs and URLs in angle brackets will automatically get turned into links. http://www.example.com or http://www.example.com and sometimes example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

Images
Here's our logo (hover to see the title text):

Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

Reference-style: 
![alt text][logo]

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"
Here's our logo (hover to see the title text):

Inline-style: alt text

Reference-style: alt text

Code and Syntax Highlighting
Code blocks are part of the Markdown spec, but syntax highlighting isn't. However, many renderers -- like Github's and Markdown Here -- support syntax highlighting. Which languages are supported and how those language names should be written will vary from renderer to renderer. Markdown Here supports highlighting for dozens of languages (and not-really-languages, like diffs and HTTP headers); to see the complete list, and how to write the language names, see the highlight.js demo page.

Inline `code` has `back-ticks around` it.
Inline code has back-ticks around it.

Blocks of code are either fenced by lines with three back-ticks ```, or are indented with four spaces. I recommend only using the fenced code blocks -- they're easier and only they support syntax highlighting.

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
 
```python
s = "Python syntax highlighting"
print s
```
 
```
No language indicated, so no syntax highlighting. 
But let's throw in a <b>tag</b>.
```
var s = "JavaScript syntax highlighting";
alert(s);
s = "Python syntax highlighting"
print s
No language indicated, so no syntax highlighting in Markdown Here (varies on Github). 
But let's throw in a <b>tag</b>.
Tables
Tables aren't part of the core Markdown spec, but they are part of GFM and Markdown Here supports them. They are an easy way of adding tables to your email -- a task that would otherwise require copy-pasting from another application.

Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3
Colons can be used to align columns.

Tables  Are Cool
col 3 is    right-aligned   $1600
col 2 is    centered    $12
zebra stripes   are neat    $1
There must be at least 3 dashes separating each header cell. The outer pipes (|) are optional, and you don't need to make the raw Markdown line up prettily. You can also use inline Markdown.

Markdown    Less    Pretty
Still   renders nicely
1   2   3
Blockquotes
> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote. 
Blockquotes are very handy in email to emulate reply text. This line is part of the same quote.

Quote break.

This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can put Markdown into a blockquote.

Inline HTML
You can also use raw HTML in your Markdown, and it'll mostly work pretty well.

<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>
Definition list
Is something people use sometimes.
Markdown in HTML
Does *not* work **very** well. Use HTML tags.
Horizontal Rule
Three or more...

---

Hyphens

***

Asterisks

___

Underscores
Three or more...

Hyphens

Asterisks

Underscores

Line Breaks
My basic recommendation for learning how line breaks work is to experiment and discover -- hit <Enter> once (i.e., insert one newline), then hit it twice (i.e., insert two newlines), see what happens. You'll soon learn to get what you want. "Markdown Toggle" is your friend.

Here are some things to try out:

Here's a line for us to start with.

This line is separated from the one above by two newlines, so it will be a *separate paragraph*.

This line is also a separate paragraph, but...
This line is only separated by a single newline, so it's a separate line in the *same paragraph*.
Here's a line for us to start with.

This line is separated from the one above by two newlines, so it will be a separate paragraph.

This line is also begins a separate paragraph, but...
This line is only separated by a single newline, so it's a separate line in the same paragraph.

(Technical note: Markdown Here uses GFM line breaks, so there's no need to use MD's two-space line breaks.)

YouTube Videos
They can't be added directly but you can add an image with a link to the video like this:

<a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE
" target="_blank"><img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
Or, in pure Markdown, but losing the image sizing and border:

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)
Referencing a bug by #bugID in your git commit links it to the slip. For example #1.
MATHS

$$
f(x) = \int_{-\infty}^\infty
    \hat f(\xi)\,e^{2 \pi i \xi x}
    \,d\xi
$$

ATTACH FILE

[email_fabrica.txt](:/01e517ea2f8f448294a2209965056860)

HORIZONTAL RULE

* * * 
