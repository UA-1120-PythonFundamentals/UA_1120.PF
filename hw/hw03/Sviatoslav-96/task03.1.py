python_phylosophy = ("""1. Beautiful {0} {1} than ugly.     
2. Explicit {0} {1} than implicit.  
3. Simple {0} {1} than complex.     
4. Complex {0} {1} than complicated.
5. Flat {0} {1} than nested.
6. Sparse {0} {1} than dense.
7. Readability counts.
8. Special cases aren't special enough to break the rules.
9. Although practicality beats purity.
10. Errors should {2} pass silently.
11. Unless explicitly silenced.
12. In the face of ambiguity, refuse the temptation to guess.
13. There should be one-- and preferably only one --obvious way to do it.
14. Although that way may not be obvious at first unless you're Dutch.
15. Now {0} {1} than {2}.
16. Although {2} {0} often {1} than *right* now.
17. If the implementation {0} hard to explain, it's a bad idea.
18. If the implementation {0} easy to explain, it may be a good idea.
19. Namespaces are one honking great idea -- let's do more of those!""")

print(python_phylosophy.format("is", "better", "never").replace("i", "&").upper())