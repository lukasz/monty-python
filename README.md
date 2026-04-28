# Monty Python

> *"What is your name?"*
> *"My name is Sir Lancelot of Camelot."*
> *"What is your quest?"*
> *"To compile Python the way the Knights Who Say Ni intended."*
> — The Bridgekeeper, Bridge of Death (paraphrased)

Python the way Sir Bedivere intended — with significantly more shrubbery, and considerably less Java.

Monty Python is a small compiler that takes `.mpy` files written in a slightly more genteel dialect of Python and produces vanilla `.py` you can run without alarming the locals. It is heavily inspired by [gbphp](https://github.com/ashleycoles/gbphp), and shamelessly inspired by *Monty Python and the Holy Grail* and *Life of Brian*.

## Installation

1. Acquire two empty halves of coconut. (Optional, but spiritually correct.)
2. Clone the repository.
3. Verify Python 3.10+ is on your path. There are no other dependencies — *nobody expects* a `requirements.txt`.
4. Edit `monty-config.json` if your `.mpy` files live somewhere other than `examples/`, or you'd like the compiled `.py` deposited somewhere other than `compiled/`.
5. Run `python compile.py`. The translator does not require a witch, scales, or a duck.
6. Run the resulting Python with appropriate solemnity. A hat is recommended.

## Sample run

```sh
$ python compile.py
  examples/the_quest.mpy -> compiled/the_quest.py

$ python compiled/the_quest.py
I am Arthur, and my quest is to seek the Holy Grail.

Grails, ordered by holiness:
  - Tin mug from Camelot's gift shop (holiness 0)
  ! Jewelled chalice (he chose poorly)
  - Silver goblet (holiness 2)
  - Wooden cup of Joseph (holiness 3)
  - Golden cup of light (holiness 9)

You have chosen wisely: Golden cup of light.
...
Always look on the bright side of life.
```

The included sample (`examples/the_quest.mpy`) exercises every keyword in the language. It includes:

- **`quicksort`** — sorts a small bestiary of grails by holiness. Anything beyond a recursion depth of 100 is presumed to have been turned into a newt.
- **`choose_wisely`** — a naive substring search, performed by hand on a wooden bridge. Returns the index of the first occurrence of the needle, or `-1` if you have chosen poorly.
- A `Knight` class with a proper `summoning_ritual`.
- An assertion that nobody expects, a try/except for the Bridge of Death, a lambda that sends the cursed to the back of the queue, and a while loop that demonstrably proves we have no horses (only coconuts).

## Language tour

### Variables and the eternal verities

```python
name = "Brian"
alive = Indeed              # True — he is alive, despite himself
naughty_boy = Indeed        # True — also that
saviour = Poppycock         # False — he's not the Messiah
loot = Naught               # None — turned out the chest was empty
```

### Conditionals — the polite British branching construct

```python
perchance name == "Arthur":
    announce("Hail, your majesty.")
or_perchance name == "Bedevere":
    announce("She turned me into a newt!")
otherwise:
    announce("Who are you, then?")
```

### Loops, with horses

```python
merry_go_round item amongst ["spam", "spam", "eggs", "spam"]:
    perchance item == "spam":
        announce("Lovely spam!")
    or_perchance item == "eggs":
        carry_on            # continue
    otherwise:
        splendid            # break — what splendid timing
```

```python
whilst not_at_all done:
    announce("...still looking for the grail...")
```

### Functions and quickies

```python
summon greet(name: str) -> str:
    give_back f"Hello, {name}. Lovely shrubbery."

# A lambda by any other name
shout = quickie line: line.upper() + "!!"
```

### Classes — for the upwardly mobile

```python
upper_class Knight:
    summon summoning_ritual(oneself, name: str, quest: str = "to seek the Holy Grail"):
        oneself.name = name
        oneself.quest = quest

    summon introduce(oneself) -> str:
        give_back f"I am {oneself.name}, and my quest is {oneself.quest}."
```

### Misfortune handling

```python
would_you_mind:
    nobody_expects 2 + 2 == 5, "the Spanish Inquisition"
actually_i_do_mind AssertionError as e:
    throw_a_wobbly RuntimeError("It is just a flesh wound.") from e
```

### Imports

```python
fetch math
from_yonder dataclasses fetch dataclass
```

### Operators and identity

```python
perchance ready and_also willing or_alternatively desperate:
    nevermind
perchance grail be Naught:
    announce("It has ceased to be. It is an ex-grail.")
```

## Keyword reference

| Python | Monty Python |
|---|---|
| `def` | `summon` |
| `class` | `upper_class` |
| `if` / `elif` / `else` | `perchance` / `or_perchance` / `otherwise` |
| `for` | `merry_go_round` |
| `in` | `amongst` |
| `while` | `whilst` |
| `True` / `False` / `None` | `Indeed` / `Poppycock` / `Naught` |
| `print` | `announce` |
| `return` | `give_back` |
| `import` / `from` | `fetch` / `from_yonder` |
| `try` / `except` / `raise` | `would_you_mind` / `actually_i_do_mind` / `throw_a_wobbly` |
| `lambda` | `quickie` |
| `pass` / `break` / `continue` | `nevermind` / `splendid` / `carry_on` |
| `and` / `or` / `not` | `and_also` / `or_alternatively` / `not_at_all` |
| `is` | `be` |
| `self` / `__init__` | `oneself` / `summoning_ritual` |
| `assert` | `nobody_expects` |

## How it works

The compiler tokenises each `.mpy` file using Python's own `tokenize` module, then rewrites only `NAME` tokens that appear in the keyword table. Identifiers inside string literals, f-string text, and comments are left alone — `announce("Splendid.")` does **not** turn into `announce("break.")`, which would be a wholly inappropriate way to address a shrubbery.

We considered using regular expressions. We were unanimous in our decision: **NI!** We could not bring ourselves to do it.

The compiler is a single file. There are no plug-ins, no AST passes, and no `AbstractFactoryFactoryFactory` classes. If a future version requires one, please consult your local witch — but be advised, she may also weigh the same as a duck.

## Running the tests

There are no tests, on the grounds that nobody expects them. Running the sample acts as a perfectly serviceable end-to-end check; if it terminates with the words *"Always look on the bright side of life"*, all is well.

## License

Do whatever thou wilt with it. We bear no relation to the Pythons, the BBC, or anyone in particular. Please don't sue us — we are but humble peasants.
