
=== Function: parse_fuzzy_date() ===

Input: Any value from the 'Expected Return Values' column of the excel file
- timedate: 12/2/24
- string: "December 12, 2025"
- string "3/15?"
- string: "next Friday"
- string: "soon"

Output: a datetime object representing the exact expected return date
- timedate: 3/22/82

Contextual Logic:
- instantiate class - stateless class(or minimally stateful)
- call parse(fuzzy_str, base_date) on each row of df
- return 

Mappings:
- "eod", "end of day" : today

Edge Cases: 
- "" -> None
- "TBD" -> None
- "32/15" -> don't crash or be weird

Uses:


Unique Values(as of 5/29/25):
1 -> 2023-12-22 00:00:00
2 -> 2023-12-23 00:00:00
4 -> 2023-09-26 00:00:00
5 -> 2022-10-04 00:00:00
6 -> 2022-10-17 00:00:00
7 -> 2022-10-20 00:00:00
9 -> 2022-10-25 00:00:00
10 -> 2022-10-26 00:00:00
11 -> 2022-10-27 00:00:00
12 -> 2023-06-02 00:00:00
13 -> 2022-11-18 00:00:00
14 -> 2022-11-21 00:00:00
15 -> 2022-12-01 00:00:00
16 -> 2022-12-05 00:00:00
17 -> 2022-12-06 00:00:00
18 -> 2022-12-08 00:00:00
19 -> 2022-12-13 00:00:00
20 -> 2022-12-14 00:00:00
21 -> 2023-06-01 00:00:00
22 -> 2023-02-01 00:00:00
23 -> 2023-01-31 00:00:00
24 -> 2023-01-16 00:00:00
25 -> 2023-02-06 00:00:00
26 -> 2023-02-22 00:00:00
27 -> 2023-02-17 00:00:00
28 -> 2023-04-20 00:00:00
29 -> 2023-03-07 00:00:00
30 -> 2023-02-23 00:00:00
31 -> 2023-03-01 00:00:00
32 -> 2023-03-10 00:00:00
33 -> 2023-03-09 00:00:00
34 -> 2023-03-31 00:00:00
35 -> 2023-01-06 00:00:00
36 -> 2023-03-15 00:00:00
37 -> 2023-12-31 00:00:00
38 -> 2023-03-20 00:00:00
39 -> 2023-06-30 00:00:00
40 -> 2023-03-29 00:00:00
41 -> 2023-04-06 00:00:00
42 -> 2023-04-17 00:00:00
43 -> 2023-04-19 00:00:00
44 -> 2023-08-31 00:00:00
45 -> 2023-05-04 00:00:00
46 -> 2023-05-15 00:00:00
47 -> 2023-05-26 00:00:00
48 -> 2023-05-16 00:00:00
49 -> 2023-05-30 00:00:00
50 -> 2023-05-11 00:00:00
51 -> 2023-05-17 00:00:00
52 -> 2023-05-24 00:00:00
53 -> 2023-05-19 00:00:00
54 -> 2023-09-01 00:00:00
55 -> 2023-06-12 00:00:00
56 -> 2023-08-21 00:00:00
57 -> 2023-08-07 00:00:00
58 -> 3033-12-21 00:00:00
59 -> 2023-12-21 00:00:00
61 -> 2023-08-17 00:00:00
62 -> 2023-08-18 00:00:00
67 -> 2023-08-24 00:00:00
71 -> 2023-09-07 00:00:00
74 -> 2024-06-01 00:00:00
77 -> 2023-09-11 00:00:00
80 -> 2023-12-26 00:00:00
81 -> 2023-09-28 00:00:00
82 -> 2023-10-12 00:00:00
83 -> 2023-10-05 00:00:00
84 -> 2023-10-16 00:00:00
85 -> 2023-10-20 00:00:00
86 -> 2023-12-16 00:00:00
87 -> 2023-11-14 00:00:00
90 -> 2024-01-30 00:00:00
93 -> 2024-03-01 00:00:00
94 -> 2024-03-02 00:00:00
97 -> 2024-03-19 00:00:00
98 -> 2024-03-21 00:00:00
101 -> 2024-05-02 00:00:00
102 -> 2024-05-08 00:00:00
105 -> 2024-06-20 00:00:00
106 -> 2024-08-10 00:00:00
107 -> 2024-07-26 00:00:00
109 -> 2025-01-03 00:00:00
111 -> 2024-09-10 00:00:00
112 -> 2024-10-15 00:00:00
113 -> 2024-09-19 00:00:00
114 -> 2024-10-22 00:00:00
115 -> 2025-01-21 00:00:00
118 -> 2025-05-30 00:00:00
119 -> 2025-05-31 00:00:00
126 -> 2025-03-17 00:00:00
127 -> 2025-04-01 00:00:00
131 -> 2025-05-05 00:00:00
132 -> 2025-05-06 00:00:00
134 -> 2025-05-26 00:00:00
135 -> 2025-05-15 00:00:00
136 -> 2025-05-23 00:00:00
137 -> 2025-08-01 00:00:00
138 -> 2025-05-27 00:00:00
139 -> 2025-05-22 00:00:00
3 -> Indefinite
8 -> 12/22/23?
60 -> End of Year
63 -> End of semester
64 -> end of semester
65 -> End of Semenster 
66 -> End of Semester
68 -> Today
69 -> today
70 -> indefinite
72 -> Indefinitely
73 -> Today 
75 -> end of semenster 
76 -> end of the sementer 
78 -> end of day
79 -> end of semester 
88 -> End of semester 
89 -> end of next semester
91 -> Indefinitely 
92 -> indefinetly
95 -> indefinitely
96 -> End of the day
99 -> indefinetely
100 -> indefinetely 
103 -> indefinetly 
104 -> Indefinetly
108 -> Summer 2025
110 -> End of Semester 
116 -> End of the Day
117 -> EOD
120 -> Inddefinitely
121 -> Indefinietly 
122 -> Until end of Spring sem
123 -> 2 weeks
124 -> 20th March
125 -> 12:15 Today
128 -> End of the week
129 -> 2 Weeks
130 -> Next week
133 -> An hour





