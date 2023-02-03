# Chapter One Exercises:

1. 1
    - Describe your own real-world example that requires sorting. Describe one that 
    requires finding the shortest distance between two points.

            -Google maps is a good example due to it's process of finding the shortest pathes from map and sort their data then choose the shortest one.
    -Other than speed, what other measures of efficiency might you need to consider in \
    a real-world setting?

            -the flexibilty of the algorithm to have wide varity of problems can apply on, memory consuming is to be consider also, because in real world other kind of data can be entered .. unexpected ones.. to be able to deal with real world surprises.
    -Select a data structure that you have seen, and discuss its strengths and limitations. 
        
        -Arrays are everywhere .. very Fast, Simple but memory monoster and can't modify it easily such inserting or deleting.
    -Suggest a real-world problem in which only the best solution will do. Then come 
    up with one in which 'approximately' the best solution is good enough. 

        -the best solution is needed always such the sorting algorithms for youtube filters or any platform interduce filters feature..
        approximately solution example when using machine learning to do something .. the whole thing is come out approximately
    
    -Describe a real-world problem in which sometimes the entire input is available 
    before you need to solve the problem, but other times the input is not entirely 
    available in advance and arrives over time. 

        -we can use youtube example again when it has to sorting now for user.. all input is available,, the other side when input come overtime it can seen in insertion sort problem like sorting when insertion for the printer in office.
2. ### Algorithms As Technology.
---

- give an example of an application that requires algorithmic content at the application level, and discuss the function of the algorithms involved.

        -As usual Youtube using algorithms at application level when it sorting content to visualize to user the suitable content.
        the function of algorithms is shown as sorting the data or content every time user open the app.

- Suppose that for inputs of size n on a particular computer, insertion sort runs in 8n2
    steps and merge sort runs in 64nlgn steps. For which values of n does insertion 
    sort beat merge sort?

    
        - we assume that: 
        then for only n smaller than 43!!!
        we used numerical solution to find root of second relation
$${8n^2 < 64 n log_2{n} :} \\
{n}<8log_2{n}:\\
$$

- What is the smallest value of n such that an algorithm whose running time is 100n2
    runs faster than an algorithm whose running time is 2
    n on the same machine?

            - is when n = 14 ,we do that numerical checking of what point the below relation has a root.
$$100X^2 - 2^X = 0$$

## Problems
---
- For each function f .n/ and time t in the following table, determine the largest 
    size n of a problem that can be solved in time t, assuming that the algorithm to 
    solve the problem takes f .n/ microseconds.

![The Full Table](.\Images\ch1.png)
---
---
---




