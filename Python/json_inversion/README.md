# JSON Inversion
by Nate Allen (github.com/nateonmission)

I frequently have data that is shaped like this:

```
{
    "age": 
    {
        "user_1": 25,
        "user_2": 35,
        "user_3": 40
    },
    "first_name":
    {
        "user_1": "John",
        "user_2": "Mary",
        "user_3": "Lee"
    }
}
```

BUT I need it to look like this:
```
{
    "user_1": 
    {
        "age": 25,
        first_name: "John"
    },
    "user_2": 
    {
        "age": 35,
        "first_name": "Mary"
    },
    "user_3":
    {
        "age": 40,
        "first_name": "Lee"
    }
}

```

This algorithm does just that.