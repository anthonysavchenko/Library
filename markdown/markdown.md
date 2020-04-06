# Markdown language

[Official documentation](https://www.markdownguide.org/)

Double trailing whitespaces and return  
mean a new line

Double returns

mean a new paragraph  


## Text decoration

**Bold text**  
*Italic text*  
***Bold and Italic text***  
~~Strikethrough text~~  
<del>Strikethrough text</del>  
Super<sup>script</sup>  
Sub<sub>script</sub>


## Links

http://hyperlink.text/  
<http://hyperlink.text/>  
[hyperlink](http://hyperlink.text/)  
[hyperlink](http://hyperlink.text/ "With tooltip text")  
**[hyperlink](http://hyperlink.text/)**  
[`hyperlinked code`](http://hyperlink.text/)  
[refereced hyperlink][label]

[label]: http://hyperlink.text/ "Tooltip text"


## Emoji

:smile:  
:+1:


## Headers

# Header 1
## Header 2
#### Header 3


## Lists

1. One
5. Two
    1. Indeted item
5. Three

    This may contain other formating

        <html>
            <head>
            </head>
        </html>


* One
+ Two
- Three
    - Indented item


- [x] One
- [ ] Two
- [ ] Three


## Code

`Inline code`

    <html>
      <body>
      </body>
    </html>

```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```


## Quotes

> ### This may contain other formating and nested quotes
>> If you don't build your dream someone will hire you to help build theirs.
>
> *Tony Gaskins*


# Horizotal Rule

***

---

___


## Tables

Header 1 | Header 2
---------|---------
Content for the first column | Content for the second column
And next row | And fourth cell


## Images

![Alt text](https://avatars0.githubusercontent.com/u/44915627 "Tooltip text")  
[![Alt text](https://avatars0.githubusercontent.com/u/44915627 "Tooltip text")](http://hyperlinked.image)


## Escape characters

``Escape `backticks` into inline code``  
\* Escaping bullets and \*\*any\*\* \[other\]\(formating\)

