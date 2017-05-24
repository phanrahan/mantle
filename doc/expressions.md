# Syntax
```
Num    ::=     /[0-9]+/
Id     ::=     /[a-zA-Z_][a-zA-Z_0-9]*/

E ::= null
    | Num
    | Id
    | E + E
    | E - E
    | - E
    | E & E
    | E | E
    | E ^ E
    | E >> E
    | E << E
    | ~ E
    | E[E]
```
