# Talent Team test assignment

Parse HTML and extract First, Last and Middle names from a certain tag.

## Additional conditions
The desired tag, which contains Name and Surname, is unique. 
It must be of type `<p>` and has a single attribute `class="full_name"`, 
there are no other such tags with the same combination in the text.
Content before and after the "cherished" tag may be arbitrary.
The desired tag can be nested in an unlimited number of other tags.

## How to analyse the content of a tag
Words are separated by spaces, a few spaces = the same as 1 space.
* If there are 3 words inside the tag - then we assume it is Last Name, First Name, Middle Name, exactly, in that order.
* 2 words is Last Name, First Name.
* 1 word is First Name.
* If there are 4 or more words inside the tag (sometimes complex names and surnames) - we consider it something complicated and incomprehensible that cannot be automatically processed, and we write some warning.


## What to get out as a result
If all went well:

"Ура! Мы нашли фамилию: Иванов, имя: Сергей, отчество: Игоревич!" или "Ура! Мы нашли фамилию: Иванов, имя: Сергей!", или "Ура! Мы нашли имя: Сергей!" 

If unsuccessful:

"Упс! Кажется, что-то слишком сложное :("