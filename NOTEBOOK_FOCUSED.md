# Focused notebook extraction

- Total cells: 233
- Markdown cells: 86
- Code cells: 90

## Cell 1 — markdown

# Step 1 -- Importing the modules

## Cell 6 — code

```python
df.head()
```

**Text output:**

```text
serial  sq1  d01  d02_group  d04  d05  d08a  d08b  d08c01  d08c02  d08c03  d08c04  d08c05  d08c06  d08c07  d08c08  d08c09  d08c10  d08c11  d08c12  d09  d10  q01_01  q01_02  q01_03  q01_04  q01_05  q01_06  q01_07  q01_08  q02  q03  q04  q0501  q0502  q0503  q0504  q0505  q0506  q0507  q0508  q0509  q0510  q0511  q0512  q0513  q0514  q06  q07  q08  q0901  q0902  q0903  q0904  q0905  q0906  q0907  q0908  q0909  q0910  q0911  q0912  q10_01  q10_02  q10_03  q10_04  q10_05  q11_01  q11_02  q11_03  q11_04  q11_05  q11_06  q11_07  q11_08  q11_09  q11_10  q11_11  q11_12  q11_13  q11_14  q12  q1301  q1302  q1303  q1304  q1305  q1306  q1307  q1308  q1309  q1310  q1311  q1312  q14_01  q14_02  q14_03  q14_04  q14_05  q15_01  q15_02  q15_03  q15_04  q15_05  q15_06  q15_07  q15_08  q15_09
0      35    2    1          2    7    2     1     2       0       0       0       0       0       0       0       1       0       0       0       0    2    2       2       1       3       4       4       3       3       3    1    1    1    1.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0  1.0  4.0  2.0    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN       1       1       1       1     NaN       1       1       3       1       1       2       1       1       1       2       1       1       1       2    2    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN       2       1       1       2       5       1       4       1       1       1       2       2       1       1
1      59    2    2          2   11    1     1     1       1       0       0       0       1       0       0       1       0       0       0       0    1    1       4       3       4       4       4       1       2       4    1    1    1    1.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0  1.0  1.0  1.0    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN       1       1       1       1     1.0       2       1       1       1       1       1       1       2       1       1       1       2       1       1    1    0.0    0.0    0.0    1.0    0.0    0.0    0.0    0.0    1.0    0.0    0.0    0.0       1       1       1       1       1       2       2       1       2       2       4       2       2       2
2      86    2    2          4   11    2     1     2       1       0       0       0       1       0       0       0       0       0       0       0    2    2       3       2       3       4       4       3       4       4    2    5    1    1.0    0.0    1.0    0.0    0.0    0.0    1.0    0.0    0.0    0.0    1.0    0.0    0.0    0.0  2.0  NaN  NaN    0.0    1.0    1.0    0.0    1.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0       1       3       2       1     NaN       4       5       4       3       3       3       4       5       5       3       4       2       2       3    2    NaN    NaN    NaN    NaN    NaN    NaN    Na
... [output truncated]
```

## Cell 7 — code

```python
df.tail()
```

**Text output:**

```text
serial  sq1  d01  d02_group  d04  d05  d08a  d08b  d08c01  d08c02  d08c03  d08c04  d08c05  d08c06  d08c07  d08c08  d08c09  d08c10  d08c11  d08c12  d09  d10  q01_01  q01_02  q01_03  q01_04  q01_05  q01_06  q01_07  q01_08  q02  q03  q04  q0501  q0502  q0503  q0504  q0505  q0506  q0507  q0508  q0509  q0510  q0511  q0512  q0513  q0514  q06  q07  q08  q0901  q0902  q0903  q0904  q0905  q0906  q0907  q0908  q0909  q0910  q0911  q0912  q10_01  q10_02  q10_03  q10_04  q10_05  q11_01  q11_02  q11_03  q11_04  q11_05  q11_06  q11_07  q11_08  q11_09  q11_10  q11_11  q11_12  q11_13  q11_14  q12  q1301  q1302  q1303  q1304  q1305  q1306  q1307  q1308  q1309  q1310  q1311  q1312  q14_01  q14_02  q14_03  q14_04  q14_05  q15_01  q15_02  q15_03  q15_04  q15_05  q15_06  q15_07  q15_08  q15_09
662     663    2    2          3   12    2     2     1       0       0       0       0       0       0       0       0       0       1       0       0    2    2       2       2       4       3       4       3       3       2    3    4    3    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN  NaN  NaN  NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN       2       3       2       2     NaN       3       4       2       3       4       3       3       4       4       4       4       4       4       4    1    0.0    1.0    0.0    0.0    0.0    1.0    0.0    0.0    0.0    0.0    0.0    0.0       4       2       3       2       4       3       3       4       4       4       3       1       3       4
663     664    3    2          3   10    2     1     1       1       0       0       0       0       0       0       1       0       0       0       0    1    2       3       2       4       4       4       3       4       4    2    2    2    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN  NaN  NaN  NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN       1       1       1       1     1.0       3       4       3       2       3       2       2       2       3       2       3       2       2       3    2    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN       2       1       1       3       4       2       2       3       2       3       3       2       1       2
664     665    3    1          6   15    2     1     2       0       0       0       0       0       0       0       0       0       1       0       0    2    2       3       2       4       4       4       4       3       3    1    3    2    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN  NaN  NaN  NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN       2       2       2       2     NaN       6       6       6       6       6       1       1       6       6       1       1       1       6       1    2    NaN    NaN    NaN    NaN    NaN    NaN
... [output truncated]
```

## Cell 8 — code

```python
df.dtypes
```

**Text output:**

```text
serial         int64
sq1            int64
d01            int64
d02_group      int64
d04            int64
d05            int64
d08a           int64
d08b           int64
d08c01         int64
d08c02         int64
d08c03         int64
d08c04         int64
d08c05         int64
d08c06         int64
d08c07         int64
d08c08         int64
d08c09         int64
d08c10         int64
d08c11         int64
d08c12         int64
d09            int64
d10            int64
q01_01         int64
q01_02         int64
q01_03         int64
q01_04         int64
q01_05         int64
q01_06         int64
q01_07         int64
q01_08         int64
q02            int64
q03            int64
q04            int64
q0501        float64
q0502        float64
q0503        float64
q0504        float64
q0505        float64
q0506        float64
q0507        float64
q0508        float64
q0509        float64
q0510        float64
q0511        float64
q0512        float64
q0513        float64
q0514        float64
q06          float64
q07          float64
q08          float64
q0901        float64
q0902        float64
q0903        float64
q0904        float64
q0905        float64
q0906        float64
q0907        float64
q0908        float64
q0909        float64
q0910        float64
q0911        float64
q0912        float64
q10_01         int64
q10_02         int64
q10_03         int64
q10_04         int64
q10_05       float64
q11_01         int64
q11_02         int64
q11_03         int64
q11_04         int64
q11_05         int64
q11_06         int64
q11_07         int64
q11_08         int64
q11_09         int64
q11_10         int64
q11_11         int64
q11_12         int64
q11_13         int64
q11_14         int64
q12            int64
q1301        float64
q1302        float64
q1303        float64
q1304        float64
q1305        float64
q1306        float64
q1307        float64
q1308        float64
q1309        float64
q1310        float64
q1311        float64
q1312        float64
q14_01         int64
q14_02         int64
q14_03         int64
q14_04         int64
q14_05         int64
q15_01         int64
q15_02         int64
q15_03         int64
q15_04         int64
q15_05         int64
q15_06         int64
q15_07         int64
q15_08         int64
q15_09         int64
dtype: object
```

## Cell 11 — code

```python
df_describe
```

**Text output:**

```text
Variable  Position                                                                                                                                                                                                                                    Label Question Number assigned  Measurement Level   Role  Column Width Alignment Print Format Write Format
0       serial         1                                                                                                                                                                                                                                   serial                        ID             Scale  Input             8     Right           F8           F8
1          sq1         3                                                                                                                                                                  SQ1. Which of the following best describes your current working status?                       SQ1           Nominal  Input             8     Right           F1           F1
2          d01         4                                                                                                                                                                                                                               D1. Gender                       D01           Nominal  Input             8     Right           F1           F1
3    d02_group         5                                                                                                                                                                                                                          D2. Age [Group]                 d02_group           Nominal  Input             8     Right           F1           F1
4          d04         7                                                                                                                                                                                       D4. Which of the following sectors do you work in?                       d04           Nominal  Input             8     Right           F2           F2
5          d05         8                                                                                                                                                                                       D5. Which of the following sectors do you work in?                       d05           Nominal  Input             8     Right           F1           F1
6         d08a        11                                                                                                                                                                   D8a. Have you worked from home at any point during the past 12 months?                      d08a           Nominal  Input             8     Right           F1           F1
7         d08b        12                                                                                                              
... [output truncated]
```

## Cell 13 — code

```python
df_classification
```

**Text output:**

```text
Value     filled  numbers      Columns                                                                                              Label                                                                                                                                                                                                                                Questions                                    classifcations
0          sq1        sq1        1        sq1_1  Currently furloughed / reduced hours / employer imposed temporary leave of absence as a result of                                                                                                                                                                  SQ1. Which of the following best describes your current working status?                                    working status
1          NaN        sq1        2        sq1_2                                         Working paid full time - working 30 hours per week or more                                                                                                                                                                  SQ1. Which of the following best describes your current working status?                                    working status
2          NaN        sq1        3        sq1_3                                   Working paid part time - working between 8 and 29 hours per week                                                                                                                                                                  SQ1. Which of the following best describes your current working status?                                    working status
3          NaN        sq1        4        sq1_4                                                         Working as a volunteer (full or part time)                                                                                                                                                                  SQ1. Which of the following best describes your current working status?                                    working status
4          NaN        sq1        5        sq1_5                                     Not working but seeking work or temporarily unemployed or sick                                                                                                                                                                  SQ1. Which of the following best describes your current working status?                                    working status
5          NaN        sq1        6        sq1_6                                                                   Not working and not seeking work                                                                                                                                                                  SQ1. Which of the following best describes your current working status?                                    working status
... [output truncated]
```

## Cell 14 — raw

```python
# Based on the question in each columns i have classified the data into certain topics that are working status, demographics, work place experience,
ethical acceptibility, ethical misconduct, outcome of unethical behaviour reporting,  Organizational Support for Ethics, erception of manager and organization on ethics,Pressures to act unethically,Attitudes toward minor rule violations,Concerns about the ethical future of work
```

## Cell 17 — code

```python
##check the unique values of all the data columns
for column in df.columns:
    print(f"Unique values in '{column}':")
    print(df[column].unique())
    print("-" * 40)
```

**Text output:**

```text
Unique values in 'serial':
[ 35  59  86  93 137 179 180 239 280 297 352 414 415 424 435 466 482 512
 547 570 575 577 578 594 598   3   6   7   8  10  15  51  53  55  65  66
  67  69  70  71  76  92 100 117 129 130 144 147 164 167 171 181 183 193
 195 199 207 208 224 226 228 232 247 256 269 296 304 305 307 311 330 337
 341 342 345 348 357 368 384 400 405 413 418 420 423 426 432 439 446 447
 459 463 464 479 492 510 521 525 535 557 568 572 573 579 605 606 607 615
 636 642 645 646 648 659   1   2   4   5   9  11  12  13  14  16  17  18
  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  36  37
  38  39  40  41  42  43  44  45  46  47  48  49  50  52  54  56  57  58
  60  61  62  63  64  68  72  73  74  75  77  78  79  80  81  82  83  84
  85  87  88  89  90  91  94  95  96  97  98  99 101 102 103 104 105 106
 107 108 109 110 111 112 113 114 115 116 118 119 120 121 122 123 124 125
 126 127 128 131 132 133 134 135 136 138 139 140 141 142 143 145 146 148
 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 165 166 168
 169 170 172 173 174 175 176 177 178 182 184 185 186 187 188 189 190 191
 192 194 196 197 198 200 201 202 203 204 205 206 209 210 211 212 213 214
 215 216 217 218 219 220 221 222 223 225 227 229 230 231 233 234 235 236
 237 238 240 241 242 243 244 245 246 248 249 250 251 252 253 254 255 257
 258 259 260 261 262 263 264 265 266 267 268 270 271 272 273 274 275 276
 277 278 279 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295
 298 299 300 301 302 303 306 308 309 310 312 313 314 315 316 317 318 319
 320 321 322 323 324 325 326 327 328 329 331 332 333 334 335 336 338 339
 340 343 344 346 347 349 350 351 353 354 355 356 358 359 360 361 362 363
 364 365 366 367 369 370 371 372 373 374 375 376 377 378 379 380 381 382
 383 385 386 387 388 389 390 391 392 393 394 395 396 397 398 399 401 402
 403 404 406 407 408 409 410 411 412 416 417 419 421 422 425 427 428 429
 430 431 433 434 436 437 438 440 441 442 443 444 445 448 449 450 451 452
 453 454 455 456 457 458 460 461 462 465 467 468 469 470 471 472 473 474
 475 476 477 478 480 481 483 484 485 486 487 488 489 490 491 493 494 495
 496 497 498 499 500 501 502 503 504 505 506 507 508 509 511 513 514 515
 516 517 518 519 520 522 523 524 526 527 528 529 530 531 532 533 534 536
 537 538 539 540 541 542 543 544 545 546 548 549 550 551 552 553 554 555
 556 558 559 560 561 562 563 564 565 566 567 569 571 574 576 580 581 582
 583 584 585 586 587 588 589 590 591 592 593 595 596 597 599 600 601 602
 603 604 608 609 610 611 612 613 614 616 617 618 619 620 621 622 623 624
 625 626 627 628 629 630 631 632 633 634 635 637 638 639 640 641 643 644
 647 649 650 651 652 653 654 655 656 657 658 660 661 662 663 664 665 666
 667]
----------------------------------------
Unique values in 'sq1':
[2 3]
----------------------------------------
Unique values in 'd01':
[1 2 3]
----------------------------------------
Unique values in 'd02_group':
[2 4 1 3 5 6]
-------------------------------------
... [output truncated]
```

## Cell 19 — markdown

## 3b Missing Values Detection

## Cell 20 — code

```python
#function for checking missing values for in any dataset along with the percentage of its missing
def check_missing_values(df):
    """
    Returns a summary of missing values in a DataFrame.
    
    Output includes:
    - Total missing values per column
    - Percentage of missing values per column
    """
    missing_count = df.isnull().sum()
    missing_percent = (df.isnull().mean() * 100).round(2)
    
    result = pd.DataFrame({
        'Missing_Count': missing_count,
        'Missing_Percent': missing_percent
    })
    
    # Filter only columns that actually have missing values
    result = result[result['Missing_Count'] > 0]
    
    return result
```

## Cell 21 — code

```python
check_missing_values(df)
```

**Text output:**

```text
Missing_Count  Missing_Percent
q0501             553            82.91
q0502             553            82.91
q0503             553            82.91
q0504             553            82.91
q0505             553            82.91
q0506             553            82.91
q0507             553            82.91
q0508             553            82.91
q0509             553            82.91
q0510             553            82.91
q0511             553            82.91
q0512             553            82.91
q0513             553            82.91
q0514             553            82.91
q06               553            82.91
q07               606            90.85
q08               606            90.85
q0901             618            92.65
q0902             618            92.65
q0903             618            92.65
q0904             618            92.65
q0905             618            92.65
q0906             618            92.65
q0907             618            92.65
q0908             618            92.65
q0909             618            92.65
q0910             618            92.65
q0911             618            92.65
q0912             618            92.65
q10_05            476            71.36
q1301             593            88.91
q1302             593            88.91
q1303             593            88.91
q1304             593            88.91
q1305             593            88.91
q1306             593            88.91
q1307             593            88.91
q1308             593            88.91
q1309             593            88.91
q1310             593            88.91
q1311             593            88.91
q1312             593            88.91
```

## Cell 23 — raw

```python
 Are these missing values at random,  completely at random and not at random 
Missing Completely At Random (MCAR), Missing At Random (MAR), and Missing Not At Random (MNAR)
need further analysis as we will not drop these columns easily
by reading the questions we find out that Q5, Q6 are connected to Q4 and futher analysis was conducted to check the options of the Q4
with respect to the missing values in perticular option and then it was dicovered that 
who are aware of the misconduct have answered Q5 and Q6
```

## Cell 24 — markdown

## 3c Investigating more into Missing Values

## Cell 25 — code

```python
q5_cols = [col for col in df.columns if col.startswith('q05')]

for col in q5_cols:
    df[f'{col}_missing'] = df[col].isnull()
    print(f"--- Missingness in {col} vs q04 ---")
    print(pd.crosstab(df[f'{col}_missing'], df['q04'], normalize='index') * 100)
    print("\n")
```

**Text output:**

```text
--- Missingness in q0501 vs q04 ---
q04                1          2         3
q0501_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.468354  2.531646


--- Missingness in q0502 vs q04 ---
q04                1          2         3
q0502_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.468354  2.531646


--- Missingness in q0503 vs q04 ---
q04                1          2         3
q0503_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.468354  2.531646


--- Missingness in q0504 vs q04 ---
q04                1          2         3
q0504_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.468354  2.531646


--- Missingness in q0505 vs q04 ---
q04                1          2         3
q0505_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.468354  2.531646


--- Missingness in q0506 vs q04 ---
q04                1          2         3
q0506_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.468354  2.531646


--- Missingness in q0507 vs q04 ---
q04                1          2         3
q0507_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.468354  2.531646


--- Missingness in q0508 vs q04 ---
q04                1          2         3
q0508_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.468354  2.531646


--- Missingness in q0509 vs q04 ---
q04                1          2         3
q0509_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.468354  2.531646


--- Missingness in q0510 vs q04 ---
q04                1          2         3
q0510_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.468354  2.531646


--- Missingness in q0511 vs q04 ---
q04                1          2         3
q0511_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.468354  2.531646


--- Missingness in q0512 vs q04 ---
q04                1          2         3
q0512_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.468354  2.531646


--- Missingness in q0513 vs q04 ---
q04                1          2         3
q0513_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.468354  2.531646


--- Missingness in q0514 vs q04 ---
q04                1          2         3
q0514_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.468354  2.531646
```

## Cell 26 — code

```python
df['q06_missing'] = df['q06'].isnull()

# Cross-tab between q06 missingness and q04 (aware of misconduct)
pd.crosstab(df['q06_missing'], df['q04'], normalize='index') * 100
```

**Text output:**

```text
q04              1          2         3
q06_missing                            
False        100.0   0.000000  0.000000
True           0.0  97.468354  2.531646
```

## Cell 27 — raw

```python
if Q04 is yes then  q5 and q6 is connect to this and answered
```

## Cell 28 — code

```python
df['q07_missing'] = df['q07'].isnull()

# Cross-tab between q06 missingness and q04 (aware of misconduct)
pd.crosstab(df['q07_missing'], df['q06'], normalize='index') * 100
```

**Text output:**

```text
q06            1.0       2.0      3.0
q07_missing                          
False        100.0   0.00000  0.00000
True           0.0  92.45283  7.54717
```

## Cell 29 — code

```python
df['q08_missing'] = df['q08'].isnull()

# Cross-tab between q06 missingness and q04 (aware of misconduct)
pd.crosstab(df['q08_missing'], df['q06'], normalize='index') * 100
```

**Text output:**

```text
q06            1.0       2.0      3.0
q08_missing                          
False        100.0   0.00000  0.00000
True           0.0  92.45283  7.54717
```

## Cell 30 — raw

```python
if q06 is yes then q07, q08 are answered
```

## Cell 31 — markdown

### Checking Missing Values for q9

## Cell 32 — code

```python
q9_cols = [col for col in df.columns if col.startswith('q09')]

for col in q9_cols:
    df[f'{col}_missing'] = df[col].isnull()
    print(f"--- Missingness in {col} vs q06 ---")
    print(pd.crosstab(df[f'{col}_missing'], df['q06'], normalize='index') * 100)
    print("\n")
```

**Text output:**

```text
--- Missingness in q0901 vs q06 ---
q06                  1.0    2.0       3.0
q0901_missing                            
False           0.000000  100.0  0.000000
True           93.846154    0.0  6.153846


--- Missingness in q0902 vs q06 ---
q06                  1.0    2.0       3.0
q0902_missing                            
False           0.000000  100.0  0.000000
True           93.846154    0.0  6.153846


--- Missingness in q0903 vs q06 ---
q06                  1.0    2.0       3.0
q0903_missing                            
False           0.000000  100.0  0.000000
True           93.846154    0.0  6.153846


--- Missingness in q0904 vs q06 ---
q06                  1.0    2.0       3.0
q0904_missing                            
False           0.000000  100.0  0.000000
True           93.846154    0.0  6.153846


--- Missingness in q0905 vs q06 ---
q06                  1.0    2.0       3.0
q0905_missing                            
False           0.000000  100.0  0.000000
True           93.846154    0.0  6.153846


--- Missingness in q0906 vs q06 ---
q06                  1.0    2.0       3.0
q0906_missing                            
False           0.000000  100.0  0.000000
True           93.846154    0.0  6.153846


--- Missingness in q0907 vs q06 ---
q06                  1.0    2.0       3.0
q0907_missing                            
False           0.000000  100.0  0.000000
True           93.846154    0.0  6.153846


--- Missingness in q0908 vs q06 ---
q06                  1.0    2.0       3.0
q0908_missing                            
False           0.000000  100.0  0.000000
True           93.846154    0.0  6.153846


--- Missingness in q0909 vs q06 ---
q06                  1.0    2.0       3.0
q0909_missing                            
False           0.000000  100.0  0.000000
True           93.846154    0.0  6.153846


--- Missingness in q0910 vs q06 ---
q06                  1.0    2.0       3.0
q0910_missing                            
False           0.000000  100.0  0.000000
True           93.846154    0.0  6.153846


--- Missingness in q0911 vs q06 ---
q06                  1.0    2.0       3.0
q0911_missing                            
False           0.000000  100.0  0.000000
True           93.846154    0.0  6.153846


--- Missingness in q0912 vs q06 ---
q06                  1.0    2.0       3.0
q0912_missing                            
False           0.000000  100.0  0.000000
True           93.846154    0.0  6.153846
```

## Cell 34 — code

```python
q13_cols = [col for col in df.columns if col.startswith('q13')]

for col in q13_cols:
    df[f'{col}_missing'] = df[col].isnull()
    print(f"--- Missingness in q13 vs q12 ---")
    print(pd.crosstab(df[f'{col}_missing'], df['q12'], normalize='index') * 100)
    print("\n")
```

**Text output:**

```text
--- Missingness in q13 vs q12 ---
q12                1          2         3
q1301_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.470489  2.529511


--- Missingness in q13 vs q12 ---
q12                1          2         3
q1302_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.470489  2.529511


--- Missingness in q13 vs q12 ---
q12                1          2         3
q1303_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.470489  2.529511


--- Missingness in q13 vs q12 ---
q12                1          2         3
q1304_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.470489  2.529511


--- Missingness in q13 vs q12 ---
q12                1          2         3
q1305_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.470489  2.529511


--- Missingness in q13 vs q12 ---
q12                1          2         3
q1306_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.470489  2.529511


--- Missingness in q13 vs q12 ---
q12                1          2         3
q1307_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.470489  2.529511


--- Missingness in q13 vs q12 ---
q12                1          2         3
q1308_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.470489  2.529511


--- Missingness in q13 vs q12 ---
q12                1          2         3
q1309_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.470489  2.529511


--- Missingness in q13 vs q12 ---
q12                1          2         3
q1310_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.470489  2.529511


--- Missingness in q13 vs q12 ---
q12                1          2         3
q1311_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.470489  2.529511


--- Missingness in q13 vs q12 ---
q12                1          2         3
q1312_missing                            
False          100.0   0.000000  0.000000
True             0.0  97.470489  2.529511
```

## Cell 36 — raw

```python
Not able to identify Any connection or pattern in Q10_05. We will drop it. As values of Q10_05 are missing at random
```

## Cell 39 — code

```python
df.head()
```

**Text output:**

```text
serial  sq1  d01  d02_group  d04  d05  d08a  d08b  d08c01  d08c02  d08c03  d08c04  d08c05  d08c06  d08c07  d08c08  d08c09  d08c10  d08c11  d08c12  d09  d10  q01_01  q01_02  q01_03  q01_04  q01_05  q01_06  q01_07  q01_08  q02  q03  q04  q0501  q0502  q0503  q0504  q0505  q0506  q0507  q0508  q0509  q0510  q0511  q0512  q0513  q0514  q06  q07  q08  q0901  q0902  q0903  q0904  q0905  q0906  q0907  q0908  q0909  q0910  q0911  q0912  q10_01  q10_02  q10_03  q10_04  q11_01  q11_02  q11_03  q11_04  q11_05  q11_06  q11_07  q11_08  q11_09  q11_10  q11_11  q11_12  q11_13  q11_14  q12  q1301  q1302  q1303  q1304  q1305  q1306  q1307  q1308  q1309  q1310  q1311  q1312  q14_01  q14_02  q14_03  q14_04  q14_05  q15_01  q15_02  q15_03  q15_04  q15_05  q15_06  q15_07  q15_08  q15_09  q0501_missing  q0502_missing  q0503_missing  q0504_missing  q0505_missing  q0506_missing  q0507_missing  q0508_missing  q0509_missing  q0510_missing  q0511_missing  q0512_missing  q0513_missing  q0514_missing  q06_missing  q07_missing  q08_missing  q0901_missing  q0902_missing  q0903_missing  q0904_missing  q0905_missing  q0906_missing  q0907_missing  q0908_missing  q0909_missing  q0910_missing  q0911_missing  q0912_missing  q1301_missing  q1302_missing  q1303_missing  q1304_missing  q1305_missing  q1306_missing  q1307_missing  q1308_missing  q1309_missing  q1310_missing  q1311_missing  q1312_missing
0      35    2    1          2    7    2     1     2       0       0       0       0       0       0       0       1       0       0       0       0    2    2       2       1       3       4       4       3       3       3    1    1    1    1.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0  1.0  4.0  2.0    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN       1       1       1       1       1       1       3       1       1       2       1       1       1       2       1       1       1       2    2    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN       2       1       1       2       5       1       4       1       1       1       2       2       1       1          False          False          False          False          False          False          False          False          False          False          False          False          False          False        False        False        False           True           True           True           True           True           True           True           True           True           True           True           True           True           True           True           True           True           True           True           True           True           True           True           True
1      59    2    2          2   11    1     1     1       1       0       0       0       1       0       0       1       0       0       0       0    1    1       4       3       4       4       4       1       2       4   
... [output truncated]
```

## Cell 40 — raw

```python
The variable Q10_05 asked whether the organization provides AI-specific ethical guidelines. Upon investigation, the variable had a disproportionately high number of "Not applicable" responses and no significant relationship with key outcome variables (e.g., speaking up behavior, observed misconduct, satisfaction after raising concerns). Since the focus of this analysis is on ethical climate and employee responses to misconduct, and not on AI-specific governance, this item was excluded from further analysis.
```

## Cell 41 — code

```python
# dropping the variables which are created ends with missing as there are of no use
# Drop all columns that end with '_missing_missing' or '_missing'
cols_to_drop = [col for col in df.columns if col.endswith('_missing') or col.endswith('_missing_missing')]
df.drop(columns=cols_to_drop, inplace=True)
```

## Cell 48 — code

```python
detect_outliers_iqr(df)
```

**Text output:**

```text
column  outlier_count                                                                                                                                                                                                                                                                                                           outliers
0       serial              0                                                                                                                                                                                                                                                                                                                 []
1          sq1            160  [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, ...]
2          d01              0                                                                                                                                                                                                                                                                                                                 []
3    d02_group              0                                                                                                                                                                                                                                                                                                                 []
4          d04              0                                                                                                                                                                                                                                                                                                                 []
5          d05              0                                                                                                                                                                                                                                                                                                                 []
6         d08a              0                                                                                                                                                                                                                                                                                                                 []
7         d08b              0                                                                                                                                                                                                                                                                                           
... [output truncated]
```

## Cell 52 — code

```python
full_summary(df)
```

**Text output:**

```text
count        mean         std  min    25%  median_describe     75%    max   skewness    kurtosis
serial     667.0  334.000000  192.690598  1.0  167.5            334.0  500.50  667.0   0.000000   -1.200000
sq1        667.0    2.239880    0.427331  2.0    2.0              2.0    2.00    3.0   1.221079   -0.510505
d01        667.0    1.466267    0.505215  1.0    1.0              1.0    2.00    3.0   0.205591   -1.783288
d02_group  667.0    3.323838    1.526567  1.0    2.0              3.0    5.00    6.0   0.055672   -1.065234
d04        667.0    8.127436    4.701633  1.0    3.0              8.0   11.00   17.0   0.127273   -0.842716
d05        667.0    1.676162    0.528541  1.0    1.0              2.0    2.00    3.0  -0.128484   -0.775494
d08a       667.0    1.334333    0.472111  1.0    1.0              1.0    2.00    2.0   0.703926   -1.509023
d08b       667.0    1.521739    0.537532  1.0    1.0              2.0    2.00    3.0   0.291556   -1.134791
d08c01     667.0    0.415292    0.493142  0.0    0.0              0.0    1.00    1.0   0.344576   -1.886935
d08c02     667.0    0.133433    0.340298  0.0    0.0              0.0    0.00    1.0   2.160868    2.677371
d08c03     667.0    0.016492    0.127452  0.0    0.0              0.0    0.00    1.0   7.610091   56.081635
d08c04     667.0    0.095952    0.294746  0.0    0.0              0.0    0.00    1.0   2.749910    5.578725
d08c05     667.0    0.131934    0.338673  0.0    0.0              0.0    0.00    1.0   2.180114    2.761169
d08c06     667.0    0.202399    0.402089  0.0    0.0              0.0    0.00    1.0   1.484726    0.205016
d08c07     667.0    0.265367    0.441860  0.0    0.0              0.0    1.00    1.0   1.065217   -0.867924
d08c08     667.0    0.343328    0.475176  0.0    0.0              0.0    1.00    1.0   0.661409   -1.567247
d08c09     667.0    0.035982    0.186385  0.0    0.0              0.0    0.00    1.0   4.994108   23.010102
d08c10     667.0    0.212894    0.409660  0.0    0.0              0.0    0.00    1.0   1.405896   -0.023535
d08c11     667.0    0.004498    0.066965  0.0    0.0              0.0    0.00    1.0  14.843461  218.984958
d08c12     667.0    0.000000    0.000000  0.0    0.0              0.0    0.00    0.0   0.000000    0.000000
d09        667.0    1.916042    0.623969  1.0    2.0              2.0    2.00    3.0   0.060166   -0.452221
d10        667.0    1.869565    0.498725  1.0    2.0              2.0    2.00    3.0  -0.251307    0.637870
q01_01     667.0    2.881559    0.940930  1.0    2.0              3.0    4.00    5.0  -0.044072   -0.628969
q01_02     667.0    2.487256    0.943320  1.0    2.0              2.0    3.00    5.0   0.548166   -0.224449
q01_03     667.0    3.820090    0.615626  1.0    4.0              4.0    4.00    5.0  -2.658596    8.376978
q01_04     667.0    3.458771    0.837930  1.0    3.0              4.0    4.00    5.0  -1.167245    1.033127
q01_05     667.0    3.710645    0.711504  1.0    4.0              4.0    4.00    5.0  -1.723347
... [output truncated]
```

## Cell 53 — raw

```python
1. Demographics (D-Series)
Variable	Insight
d01 (Gender)	Low variability (std ≈ 0.5), slight skew toward one gender. Likely binary or 3 categories (mean ≈ 1.46).
d02_group (Age group)	Mean ≈ 3.3 suggests most respondents are in middle age brackets. Covers 6 levels.
d04 (Years in organization)	Broad range (1–17), avg ≈ 8.13 years; moderate spread. Experience level varies substantially.
d05 (Employment type?)	Mean ≈ 1.67, again low variability. Indicates mostly one group (likely permanent/full-time).
 2. COVID & Ethics Experience (D8a–D10)
Variable	Insight
d08a, d08b	Binary/categorical, showing moderate agreement to statements. d08a has higher skew.
d08c01–d08c12	Very low mean values (mostly ≤ 0.3), high skewness and kurtosis, especially d08c03, d08c11, d08c12. Suggests rare events. Many are likely binary with majority "No".
d09, d10	Limited range (1–3), avg ≈ 2; moderate agreement or awareness. Useful for organizational culture aspects.
 3. Ethics Pressure & Observations (Q-Series)
Variable	Insight
q04 (awareness of misconduct)	Mean ≈ 1.85 on a 3-point scale => majority responded "No" or "Prefer not to say".
q06 (spoke up)	Mean = 1.5 ⇒ close split between speaking up and not speaking up (on yes=1 / no=2 coding).
q07, q08 (Satisfaction, outcomes)	Low response count (n=61), so interpret with caution; average satisfaction is moderate.
q12 (pressure to compromise ethics)	Mean ≈ 1.91 ⇒ most respondents said "No", confirming a low rate of reported pressure.
q13	Low means & high skew ⇒ only those who felt pressure answered (as expected). Responses sparse.
 4. Observed Misconduct (Q0501–Q0514)
Insight
High skewness & low mean across all — consistent with very rare events.
Kurtosis is very high in some (q0510, q0512, q0513) ⇒ extreme outlier risk or only a few true responses.
These values confirm your prior judgment to connect them with q04 == 1. Definitely MNAR pattern.
 5. Organizational Controls (Q10, Q11)
Variable	Insight
q10_01–q10_04	Mean ≈ 1.5; moderate agreement that org provides policies and training. Slight positive skew.
q11_01–q11_14	Most means range 2–3; typical 6-point Likert scale responses. Some skewed left, indicating low ratings (especially on support & protection mechanisms).
 6. Attitudes & Culture (Q14, Q15)
Insight
q14_05 has highest mean ≈ 4.09 (positive perception).
Skewness for most values ranges from ≈ 0.1 to 1.0, indicating moderate agreement across respondents.
No severe skew or kurtosis in this block — these are statistically well-behaved Likert scales.
These can be used for group comparison, correlation, or even index creation.
 7. Special Notes on Distribution

Outliers likely exist in rare-event columns (e.g., d08c03, q0510, q0910, q1312).

Skewness > 1 or < -1 and kurtosis > 3 ⇒ highly non-normal data. Considered when using statistical tests.

Binary/Missing blocks: many columns are dominated by 0/1 values — must handle them separately for visualizations.
```

## Cell 57 — markdown

## 5a Univariate Analysis

## Cell 60 — code

```python
# Mapping numeric values to labels
working_status_map = {
    1: 'Furloughed/Leave (COVID-19)',
    2: 'Working Full-Time (≥30 hrs)',
    3: 'Working Part-Time (8–29 hrs)',
    4: 'Volunteer (FT/PT)',
    5: 'Unemployed / Seeking Work',
    6: 'Not Working / Not Seeking'
}

# Apply mapping to a copy of the column
working_status_labels = df['sq1'].map(working_status_map)

# Get value counts
working_status_counts = working_status_labels.value_counts(dropna=False)
labels = working_status_counts.index
sizes = working_status_counts.values
total = sizes.sum()

# Create labels with counts and percentages
labels_with_values = [f'{label} ({count}, {count/total:.1%})' for label, count in zip(labels, sizes)]

# Custom color palette
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f']

# Plot pie chart
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels_with_values, autopct=None, startangle=140,
        colors=colors[:len(sizes)], wedgeprops={'edgecolor': 'white'})
plt.title('SQ1: Current Working Status Distribution')
plt.axis('equal')  # Ensures pie is circular
plt.tight_layout()
plt.show()
```

**Text output:**

```text
<Figure size 600x600 with 1 Axes>
```

## Cell 61 — raw

```python
The pie chart illustrates the distribution of respondents based on their current working status:

- **76%** (n = 507) of respondents are **working full-time** (≥30 hours/week).
- **24%** (n = 160) of respondents are **working part-time** (8–29 hours/week).

This indicates that the majority of the surveyed population is engaged in full-time employment.

Since the dataset contains only these two categories, it appears that the survey sample may have been filtered to include only employed individuals. This is worth noting in the context of further analysis—particularly when exploring organizational behavior, workplace ethics, or speaking-up culture.
```

## Cell 63 — markdown

#### D1. Gender

## Cell 64 — code

```python
# Define mapping for gender
gender_labels = {
    1: 'Male',
    2: 'Female',
    3: 'Other',
    4: 'Prefer not to say'
}

# Map gender labels
df['gender_labeled'] = df['d01'].map(gender_labels)
# Get counts and percentages
gender_counts = df['gender_labeled'].value_counts(dropna=False)
total_gender = gender_counts.sum()
labels_with_percents = [f"{label} ({count}, {count/total_gender:.1%})" for label, count in zip(gender_counts.index, gender_counts.values)]
# Custom color palette
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3']

plt.figure(figsize=(5, 5))
plt.pie(gender_counts.values, labels=labels_with_percents, colors=colors[:len(gender_counts)],
        autopct=None, startangle=140, wedgeprops={'edgecolor': 'white'})
plt.title('D01: Gender Distribution')
plt.axis('equal')
plt.tight_layout()
plt.show()
```

**Text output:**

```text
<Figure size 500x500 with 1 Axes>
```

## Cell 65 — raw

```python
### D01: Gender Distribution

The pie chart shows the gender breakdown of respondents:

- 53.7% identify as Male
- 46% identify as Female
- A small percentage chose "Other" or "Prefer not to say" which is 0.03%

This demographic context is helpful for understanding how perspectives on ethical behavior and workplace culture might differ across gender lines in later analysis.
```

## Cell 66 — markdown

#### D2. Age [Group]

## Cell 67 — code

```python

# Define mapping
age_group_mapping = {
    1: '18–24',
    2: '25–34',
    3: '35–44',
    4: '45–54',
    5: '55–64',
    6: '65+',
    7: 'Refused'
}

# Apply mapping
df['age_group_labeled'] = df['d02_group'].map(age_group_mapping)

# Set correct order
age_group_order = ['18–24', '25–34', '35–44', '45–54', '55–64', '65+', 'Refused']

# Get counts and percentage
age_counts = df['age_group_labeled'].value_counts().reindex(age_group_order)
age_percents = (age_counts / age_counts.sum() * 100).round(1)
# Combine into a DataFrame
age_summary = pd.DataFrame({
    'Count': age_counts,
    'Percentage': age_percents
})


# Plot horizontal bar chart
plt.figure(figsize=(9, 5))
sns.barplot(x=age_summary['Count'], y=age_summary.index, palette='Set2')

# Annotate with count and percentage
for i, (count, percent) in enumerate(zip(age_summary['Count'], age_summary['Percentage'])):
    plt.text(count + 2, i, f'{count} ({percent}%)', va='center')

plt.title('D02: Age Group Distribution (Count & %)')
plt.xlabel('Number of Respondents')
plt.ylabel('Age Group')
plt.tight_layout()
plt.show()
```

**Text output:**

```text
<Figure size 900x500 with 1 Axes>
```

## Cell 68 — raw

```python
📊 D02: Age Group Distribution – Insights

The horizontal bar chart illustrates the distribution of respondents across different age groups. Key insights include:

The largest age group is 45–54 years, accounting for 21.3% of the respondents (142 individuals).

This is followed by:

25–34 years: 19.9% (133 respondents)

35–44 years: 18.6% (124 respondents)

55–64 years: 17.5% (117 respondents)

18–24 years: 14.4% (96 respondents)

65+ years: 8.2% (55 respondents)

The "Refused" category has no valid responses.

🔍 This suggests the survey is well-represented by mid-career professionals (25–54 years), making up nearly 60% of the dataset. This demographic may have higher exposure to organizational ethical practices, which is useful context for further analysis.
```

## Cell 70 — code

```python
# Mapping codes to labels
sector_map = {
    1: 'Retail',
    2: 'Production',
    3: 'Public Admin & Defence',
    4: 'Construction',
    5: 'Agriculture',
    6: 'Motor Trades',
    7: 'Finance & Insurance',
    8: 'Health',
    9: 'Education',
    10: 'Professional & Technical',
    11: 'Information & Communication',
    12: 'Business Admin & Support',
    13: 'Transport & Storage',
    14: 'Accommodation & Food',
    15: 'Property',
    16: 'Wholesale',
    17: 'Arts, Entertainment & Others',
    18: 'Refused'
}

# Apply label mapping
df['sector_label'] = df['d04'].map(sector_map)

# Count and percent
sector_counts = df['sector_label'].value_counts(dropna=False)
sector_percent = (sector_counts / sector_counts.sum()) * 100
sector_summary = pd.DataFrame({'Count': sector_counts, 'Percentage': sector_percent.round(1)})

# Sort values for plotting
sector_summary_sorted = sector_summary.sort_values(by='Count', ascending=False)

# Plot
plt.figure(figsize=(8, 6))
sns.barplot(x='Count', y=sector_summary_sorted.index, data=sector_summary_sorted, palette='coolwarm')

# Add text on bars
for i, (count, pct) in enumerate(zip(sector_summary_sorted['Count'], sector_summary_sorted['Percentage'])):
    plt.text(count + 1, i, f'{count} ({pct}%)', va='center')

plt.title('D04: Sector Distribution (Count & %)', fontsize=14)
plt.xlabel('Number of Respondents')
plt.ylabel('Sector')
plt.tight_layout()
plt.show()
```

**Text output:**

```text
<Figure size 800x600 with 1 Axes>
```

## Cell 71 — raw

```python
The horizontal bar chart visualizes the distribution of respondents across various employment sectors:

- The **Health sector** has the highest representation, accounting for **13%** (n = 87) of respondents.
- **Education (11.2%)** and **Retail (10%)** follow closely, indicating a strong presence of public service and consumer sectors.
- Sectors such as **Motor Trades (0.6%)**, **Agriculture (0.7%)**, and **Property (1.6%)** have minimal representation in the sample.

This distribution reflects a broad mix of industries, though the majority of participants are concentrated in healthcare, education, and retail-related roles.

These insights help contextualize organizational behavior and ethical climate analysis, as workplace norms may vary significantly by sector.
```

## Cell 74 — code

```python
# Mapping D05 codes to sector type labels
sector_type_map = {
    1: 'Public Sector',
    2: 'Private Sector',
    3: 'Third/Voluntary Sector',
    4: 'Refused'
}

# Apply mapping (replace 'd05' with the actual column name if different)
df['d05_labeled'] = df['d05'].map(sector_type_map)

# Count and percentage
sector_counts = df['d05_labeled'].value_counts(dropna=False)
sector_percent = round(sector_counts / sector_counts.sum() * 100, 1)

# Create formatted labels for bar plot
sector_labels = [f"{sector} ({count}, {percent}%)"
                 for sector, count, percent in zip(sector_counts.index, sector_counts.values, sector_percent)]

# Plot horizontal bar chart
plt.figure(figsize=(7, 4))
sns.barplot(x=sector_counts.values, y=sector_counts.index, palette='coolwarm')

# Add text labels to the bars
for i, (count, percent) in enumerate(zip(sector_counts.values, sector_percent)):
    plt.text(count + 1, i, f"{count} ({percent}%)", va='center')

plt.title('D05: Sector Type Distribution/Ownership (Count & %)')
plt.xlabel('Number of Respondents')
plt.ylabel('Sector Type')
plt.tight_layout()
plt.show()
```

**Text output:**

```text
<Figure size 700x400 with 1 Axes>
```

## Cell 75 — raw

```python
D05: Sector Type Distribution / Ownership – Insights

The Private Sector dominates the employment landscape, with 411 respondents, representing 61.6% of the sample.

The Public Sector is the second largest, with 236 respondents or 35.4% of the total.

Only 3.0% (20 respondents) are from the Third/Voluntary Sector, indicating underrepresentation in this domain.

This distribution suggests that most participants are employed in for-profit, private organizations, which may influence their perceptions of ethics, reporting mechanisms, and workplace culture.

The near 2:1 ratio between private and public sector employees could affect sector-wise comparisons in subsequent analysis (e.g., ethics training, reporting confidence, etc.).
```

## Cell 77 — raw

```python
D8a. Have you worked from home at any point during the past 12 months?
D8b. Were you considered a 'key worker' during the Covid-19 pandemic?
D8c. What impact, if any, have the restrictions put in place to stop the spread of Covid-19 had on your work life? - The amount of time I have spent working from home has increased compared to before Covid-19
D8c. What impact, if any, have the restrictions put in place to stop the spread of Covid-19 had on your work life? - I have benefitted from the financial incentives provided by the Government (e.g. furlough schemes<br/>or similar)
D8c. What impact, if any, have the restrictions put in place to stop the spread of Covid-19 had on your work life? - I lost my job
D8c. What impact, if any, have the restrictions put in place to stop the spread of Covid-19 had on your work life? - I had to shield/isolate
D8c. What impact, if any, have the restrictions put in place to stop the spread of Covid-19 had on your work life? - It reduced my opportunities to develop my career
D8c. What impact, if any, have the restrictions put in place to stop the spread of Covid-19 had on your work life? - It has made me feel less motivated about work
D8c. What impact, if any, have the restrictions put in place to stop the spread of Covid-19 had on your work life? - My mental health has been negatively impacted
D8c. What impact, if any, have the restrictions put in place to stop the spread of Covid-19 had on your work life? - It has allowed me to have a better work-life balance
D8c. What impact, if any, have the restrictions put in place to stop the spread of Covid-19 had on your work life? - Other
D8c. What impact, if any, have the restrictions put in place to stop the spread of Covid-19 had on your work life? - No significant impact
D8c. What impact, if any, have the restrictions put in place to stop the spread of Covid-19 had on your work life? - Prefer not to say
D8c. What impact, if any, have the restrictions put in place to stop the spread of Covid-19 had on your work life? - Don't know
D9. Has your company adopted Artificial Intelligence (AI) in its business processes?
D10. Do you interact with Artificial Intelligence (AI) technologies in your work environment?
```

## Cell 79 — code

```python
# Mapping raw values to labels
d08a_mapping = {
    1: 'Yes',
    2: 'No',
    3: 'Refused'
}
df['d08a_label'] = df['d08a'].map(d08a_mapping)

# Count and percentage
d08a_counts = df['d08a_label'].value_counts(dropna=False)
d08a_percent = (d08a_counts / d08a_counts.sum() * 100).round(1)

# Plot
plt.figure(figsize=(6, 4))
sns.barplot(x=d08a_counts.values, y=d08a_counts.index, palette='pastel')

# Annotate bars
for i, (count, percent) in enumerate(zip(d08a_counts.values, d08a_percent.values)):
    plt.text(count + 2, i, f'{count} ({percent}%)', va='center')

plt.title('D8a: Worked from Home in Past 12 Months')
plt.xlabel('Number of Respondents')
plt.ylabel('Response')
plt.tight_layout()
plt.show()
```

**Text output:**

```text
<Figure size 600x400 with 1 Axes>
```

## Cell 80 — raw

```python
D8a: Have You Worked from Home in the Past 12 Months?

A majority of respondents reported working from home in the past year.

This suggests that remote work remains a significant part of the post-COVID workforce landscape.

These findings can guide further exploration, especially for analyzing if remote workers differ in their views on ethical culture, reporting misconduct, or access to ethical resources.
```

## Cell 83 — raw

```python
D8b: Were You Considered a 'Key Worker' During COVID-19?

The majority of respondents reported they were not considered key workers during the pandemic.

A notable proportion identified as key workers, which may shape their experiences with workplace ethics, pressure, and support.

This question adds valuable segmentation for deeper cross-analysis (e.g., key workers vs. non-key workers on reporting misconduct or ethical climate).
```

## Cell 87 — raw

```python
📊 Chart 1: Bar Charts for Individual Impacts (Yes/No Responses)

Each subplot shows how many respondents selected "Yes" or "No" for each potential work-life impact due to Covid-19:

Most Reported Impacts:

More Work-from-Home: 41.5% reported increased remote work time.

Better Work-Life Balance: Reported by 34.3%, suggesting remote work may have had positive outcomes.

Mental Health Decline: 26.5% experienced a decline in mental health.

Feeling Less Motivated: 20.2% said motivation dropped.

Career Development Reduced: 13.2% felt fewer opportunities for growth.

Least Reported Impacts:

Lost Job: Only 1.6% reported losing their job.

Prefer Not to Say and Don’t Know: Minimal responses here, indicating most respondents had clear experiences.

Neutral/No Impact:

21.3% reported No Significant Impact, indicating a notable portion were unaffected.
```

## Cell 89 — raw

```python
🧩 Chart 2: Top 15 Reported Combinations of Impacts

This UpSet-style plot visualizes the most common combinations of impacts:

Common Combinations:

The most frequent combination (142 respondents) was: More WFH + Better Work-Life Balance — a positive synergy.

Mental Health Decline + Less Motivated appears multiple times across top combinations, highlighting recurring mental health challenges.

Several combinations include Fewer Career Opportunities, indicating structural work limitations during the pandemic.

Negative Impact Clusters:

Combinations like Mental Health Decline + Career Dev. Reduced + Less Motivated appear frequently — showing that mental health issues often coincided with career dissatisfaction.

Diverse Experience:

The range of combinations (some with up to 4 impacts) demonstrates that the pandemic's effect on work life was highly varied and multifaceted across individuals.

🧠 Summary Insights:

Remote work was the most prominent change, with positive spillovers like better work-life balance.

However, mental health and motivation challenges were widely reported, especially in combination.

Career development and isolation were also significant but less reported.

The low percentage of job loss suggests economic protections (like furlough schemes) may have been effective.

Multidimensional analysis reveals that impacts rarely occurred in isolation.
```

## Cell 91 — code

```python
# ================================================================
# Q3 ANALYSIS (NO PIE CHART):
# "Considering your organisation's response to the Covid-19 pandemic,
# would you say that your opinion on how ethically your organisation behaves has ...?"
# ================================================================

# ---------------------------
# 1. Define response mapping
# ---------------------------
q3_mapping = {
    1: "Significantly improved",
    2: "Slightly improved",
    3: "Stayed the same",
    4: "Slightly worsened",
    5: "Significantly worsened",
    6: "Prefer not to say"
}

# ---------------------------
# 2. Apply mapping
# ---------------------------
df["q03_label"] = df["q03"].map(q3_mapping)

# ---------------------------
# 3. Frequency & percentage table
# ---------------------------
q3_freq = df["q03_label"].value_counts(dropna=False).reindex(q3_mapping.values())
q3_percent = df["q03_label"].value_counts(normalize=True, dropna=False).reindex(q3_mapping.values()) * 100

q3_summary = pd.DataFrame({
    "Count": q3_freq,
    "Percentage": q3_percent.round(2)
})

print("\n============== Q3 SUMMARY TABLE ==============\n")
display(q3_summary)

# ---------------------------
# 4. Bar Chart (Only Visualization)
# ---------------------------
plt.figure(figsize=(9,5))
q3_freq.plot(kind="bar", color="#4C72B0")

plt.title("Q3: Ethical Perception Change Due to Covid-19 Response")
plt.xlabel("Response Options")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# ================================================================
# END OF Q3 ANALYSIS (Pie Chart Removed)
# ================================================================
```

**Text output:**

```text
============== Q3 SUMMARY TABLE ==============
```

```text
Count  Percentage
q03_label                                
Significantly improved     79       11.84
Slightly improved         152       22.79
Stayed the same           384       57.57
Slightly worsened          35        5.25
Significantly worsened     13        1.95
Prefer not to say           4        0.60
```

```text
<Figure size 900x500 with 1 Axes>
```

## Cell 92 — raw

```python
“The distribution of Q3 responses demonstrates that the organisation’s Covid-19 response was assessed positively by a substantial proportion of employees, with 34.6% reporting an improvement in ethical behaviour. The majority (57.6%) experienced no change, indicating a stable ethical climate despite crisis pressures. Only 7.2% perceived a deterioration, suggesting isolated pockets of dissatisfaction that warrant further investigation. The small ‘Prefer not to say’ response (0.6%) may indicate sensitivity or a lack of psychological safety around critiquing organisational decisions. Overall, the Covid-19 response appears to have strengthened rather than weakened ethical perception.”
```

## Cell 94 — markdown

#### D9. Has your company adopted Artificial Intelligence (AI) in its business processes?

## Cell 95 — code

```python

# Step 1: Map the one-hot columns into a single response
def consolidate_d09(row):
    if row['d09'] == 1:
        return 'Yes'
    elif row['d09'] == 2:
        return 'No'
    elif row['d09'] == 3:
        return "Don't know"
    else:
        return 'Missing'

df['AI_Adoption'] = df.apply(consolidate_d09, axis=1)

# Step 2: Count & Percent
ai_counts = df['AI_Adoption'].value_counts()
ai_percent = round((ai_counts / ai_counts.sum()) * 100, 1)

# Step 3: Plot
plt.figure(figsize=(7, 5))
sns.barplot(x=ai_counts.index, y=ai_counts.values, palette='crest')

# Add count and %
for i, (count, pct) in enumerate(zip(ai_counts.values, ai_percent.values)):
    plt.text(i, count + 5, f'{count} ({pct}%)', ha='center', fontweight='bold')

plt.title('D09: AI Adoption in Company Business Processes', fontsize=14)
plt.xlabel('Response')
plt.ylabel('Number of Respondents')
plt.tight_layout()
plt.show()
```

**Text output:**

```text
<Figure size 700x500 with 1 Axes>
```

## Cell 96 — raw

```python
A significant portion of respondents reported that their company has adopted AI in business processes.

A notable percentage still said "No", indicating room for digital transformation across sectors.

A smaller group chose "Don’t know", suggesting a possible lack of awareness about AI implementation at their workplace.
```

## Cell 97 — markdown

#### D10. Do you interact with Artificial Intelligence (AI) technologies in your work environment?

## Cell 98 — code

```python


# Step 1: Combine one-hot columns into a single categorical column
def consolidate_d10(row):
    if row['d10'] == 1:
        return 'Yes'
    elif row['d10'] == 2:
        return 'No'
    elif row['d10'] == 3:
        return "Don't know"
    else:
        return 'Missing'

df['AI_Interaction'] = df.apply(consolidate_d10, axis=1)

# Step 2: Count and percentage
interaction_counts = df['AI_Interaction'].value_counts()
interaction_percent = round((interaction_counts / interaction_counts.sum()) * 100, 1)

# Step 3: Plot the distribution
plt.figure(figsize=(7, 5))
sns.barplot(x=interaction_counts.index, y=interaction_counts.values, palette='light:#5A9')

# Add count and percentage on bars
for i, (count, pct) in enumerate(zip(interaction_counts.values, interaction_percent.values)):
    plt.text(i, count + 5, f'{count} ({pct}%)', ha='center', fontweight='bold')

plt.title('D10: Interaction with AI Technologies at Work', fontsize=14)
plt.xlabel('Response')
plt.ylabel('Number of Respondents')
plt.tight_layout()
plt.show()
```

**Text output:**

```text
<Figure size 700x500 with 1 Axes>
```

## Cell 99 — raw

```python
A notable share of respondents reported interacting with AI technologies at work, highlighting its growing presence in daily operations.

A majority may still report no interaction, suggesting many roles remain unaffected or unaware.

The "Don’t know" group may indicate uncertainty about what qualifies as AI, pointing to a need for internal training or communication.
```

## Cell 101 — code

```python
# Assuming df is your DataFrame
q01_columns = ['q01_01', 'q01_02', 'q01_03', 'q01_04', 'q01_05', 'q01_06', 'q01_07', 'q01_08']

# Mapping for Likert responses
likert_labels = {
    1: 'Totally acceptable',
    2: 'Fairly acceptable',
    3: 'Not very acceptable',
    4: 'Totally unacceptable',
    5: "Don't know"
}

# Titles for each question
q01_titles = {
    'q01_01': 'Taking stationery for personal use',
    'q01_02': 'Using printer for personal items',
    'q01_03': 'Sexual advances to colleague',
    'q01_04': 'Claiming fuel expenses for personal use',
    'q01_05': 'Charging entertainment to expenses',
    'q01_06': 'Pretending to be sick',
    'q01_07': 'Exaggeration of travel expenses',
    'q01_08': 'Favouritism in hiring/contracts'
}

# Prepare subplots
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(15, 16))
axes = axes.flatten()

# Plot each Q01 item
for i, col in enumerate(q01_columns):
    ax = axes[i]
    counts = df[col].map(likert_labels).value_counts(normalize=True).reindex(likert_labels.values()) * 100
    sns.barplot(x=counts.values, y=counts.index, palette='coolwarm', ax=ax)

    for j, value in enumerate(counts.values):
        ax.text(value + 1, j, f'{value:.1f}%', va='center', fontweight='bold')

    ax.set_title(q01_titles[col], fontsize=12)
    ax.set_xlim(0, 100)
    ax.set_xlabel('Percentage')
    ax.set_ylabel('Response')

# Clean layout
plt.tight_layout()
plt.show()
```

**Text output:**

```text
<Figure size 1500x1600 with 8 Axes>
```

## Cell 102 — raw

```python
🔍 Interpretation & Insights

Clear Moral Boundaries Exist for Severe Misconduct

“Making sexual advances towards a colleague” is deemed “Totally unacceptable” by 84.1%, showing a strong ethical consensus.

Similarly, “Charging entertainment to expenses” (72.3%) and “Claiming personal fuel expenses” (57.6%) also draw strong disapproval.

Moral Ambiguity in Minor Infractions

“Taking stationery” and “Using printer for personal items” show mixed views, with around 30–36% saying “Fairly” or “Totally acceptable.”

These might be seen as “low-stakes” actions where ethical norms vary.

Gray Areas in Sick Leave Abuse & Expense Exaggeration

Actions like “Pretending to be sick” or “Minor exaggeration of travel expenses” show fairly divided opinions. ~40% find it “Totally unacceptable,” but over 35% are more lenient.

This may reflect rationalization during high-pressure work environments.

Nepotism Rejection is Strong

“Favoring friends/family in recruitment” was considered “Totally unacceptable” by 61% – indicating ethical concern around fairness and meritocracy
```

## Cell 105 — code

```python
# ================================================================
# Q2 ANALYSIS: "In your organisation's daily operations, 
# would you say that honesty is practised ... ?"
# ================================================================

# ---------------------------
# 1. Define mapping
# ---------------------------
q2_mapping = {
    1: "Always",
    2: "Frequently",
    3: "Occasionally",
    4: "Rarely",
    5: "Never"
}

# ---------------------------
# 2. Apply mapping
# ---------------------------
df["q02_label"] = df["q02"].map(q2_mapping)

# ---------------------------
# 3. Frequency & percentage table
# ---------------------------
q2_freq = df["q02_label"].value_counts(dropna=False).reindex(q2_mapping.values())
q2_percent = df["q02_label"].value_counts(normalize=True, dropna=False).reindex(q2_mapping.values()) * 100

q2_summary = pd.DataFrame({
    "Count": q2_freq,
    "Percentage": q2_percent.round(2)
})

print("\n============== Q2 SUMMARY TABLE ==============\n")
display(q2_summary)

# ---------------------------
# 4. Bar Chart
# ---------------------------
plt.figure(figsize=(8,5))
q2_freq.plot(kind="bar", color="#4C72B0")

plt.title("Q2: Honesty Practised in Organisation")
plt.xlabel("Response Options")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.6)
plt.tight_layout()
plt.show()


# ================================================================
# END OF Q2 ANALYSIS
# ================================================================
```

**Text output:**

```text
============== Q2 SUMMARY TABLE ==============
```

```text
Count  Percentage
q02_label                      
Always          237       35.53
Frequently      340       50.97
Occasionally     58        8.70
Rarely           13        1.95
Never             4        0.60
```

```text
<Figure size 800x500 with 1 Axes>
```

## Cell 106 — raw

```python
🎯 1. Strong Perception of Ethical Behaviour in Daily Operations

More than 86% of respondents believe honesty is Always or Frequently practised.
This indicates:

A strong ethical climate

High perceived trust within the organisation

A baseline for ethical decision-making and transparency

This aligns with established literature suggesting that employees are more likely to observe and report misconduct when they perceive honesty in leadership and peers.

🎯 2. Moderate Positive Bias Likely Present (Social Desirability Effect)

Ethics-related questions often trigger social desirability bias, where respondents lean toward socially acceptable answers.

The extremely low percentage for “Never” (0.6%) suggests:

Employees may hesitate to state negative views

Fear of judgement or concerns about traceability of responses

Organizational culture may discourage speaking negatively

This insight is valuable to critique the data collection limitations in your assignment.

🎯 3. Middle Category (‘Occasionally’) Indicates Ethical Inconsistency

The 8.70% selecting “Occasionally” signals that:

Honesty may not be uniformly practised across teams

Some departments or managers may behave inconsistently

Ethical culture might vary by job role or hierarchy

This group is important for bivariate analysis (e.g., by gender, age, or sector) to uncover where ethical inconsistency is higher.

🎯 4. Very Low Negative Responses Suggest Hidden Ethical Issues

Only 1.95% (Rarely) and 0.6% (Never) reported honesty is not practised.

Low negative responses could mean:

Actual strong culture OR

Employees avoid criticising leadership due to fear of retaliation

Limited psychological safety

Under-reporting of misconduct perceptions

This is an essential point for your assignment’s data bias discussion.

🎯 5. Gap Between “Always” and “Frequently” is Meaningful

Although perception is positive overall:

“Always”: 35.53%

“Frequently”: 50.97%

This gap shows honesty is not absolute; nearly half the workforce sees honesty as conditional or situational.

This is a critical nuance in professional ethics discussions:

Employees trust the organisation, but not unconditionally.

🎯 6. Implications for Decision-Making & Organisational Ethics

High honesty perception correlates with:

Higher job satisfaction

Lower employee turnover

Increased reporting of ethical violations

Stronger alignment with organisational values

This insight strengthens your later multivariate analysis, especially when checking relationships between:

Q2 × Q11 (Manager ethics)

Q2 × Q6–Q8 (Misconduct reporting)

Q2 × Q14 (Attitude toward minor violations)
```

## Cell 107 — markdown

### Ethical misconduct Awareness

## Cell 108 — markdown

#### Q4. During the past year at work, have you been aware of any conduct by your employer or colleagues that you thought violated either the law or your organisation's ethical standards?

## Cell 109 — code

```python
# ---------------------------
# 1. Define response mapping
# ---------------------------
q4_mapping = {
    1: "Yes",
    2: "No",
    3: "Prefer not to say"
}

# ---------------------------
# 2. Apply mapping
# ---------------------------
df["q04_label"] = df["q04"].map(q4_mapping)

# ---------------------------
# 3. Frequency & percentage table
# ---------------------------
q4_freq = df["q04_label"].value_counts(dropna=False).reindex(q4_mapping.values())
q4_percent = df["q04_label"].value_counts(normalize=True, dropna=False).reindex(q4_mapping.values()) * 100

q4_summary = pd.DataFrame({
    "Count": q4_freq,
    "Percentage": q4_percent.round(2)
})

print("\n============== Q4 SUMMARY TABLE ==============\n")
display(q4_summary)

# ---------------------------
# 4. Bar Chart
# ---------------------------
plt.figure(figsize=(8,5))
q4_freq.plot(kind="bar", color="#4C72B0")

plt.title("Q4: Awareness of Misconduct in the Past Year")
plt.xlabel("Response Options")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
```

**Text output:**

```text
============== Q4 SUMMARY TABLE ==============
```

```text
Count  Percentage
q04_label                           
Yes                  114       17.09
No                   539       80.81
Prefer not to say     14        2.10
```

```text
<Figure size 800x500 with 1 Axes>
```

## Cell 110 — raw

```python
“Awareness of misconduct was reported by 17.1% of respondents, indicating that ethical breaches are relatively visible within the organisation. While 80.8% reported no awareness of violations, this does not necessarily confirm the absence of misconduct, as it may instead reflect limited exposure, concealment of unethical behaviour, or variation in employee understanding of ethical norms. A further 2.1% selected ‘Prefer not to say’, suggesting residual fear or concerns about expressing opinions on organisational ethics. These findings highlight both the presence of unethical conduct and potential limitations in psychological safety and data validity.”
```

## Cell 111 — code

```python
# ================================================================
# Q5 MULTI-PLOT VISUALISATION (YES/NO FOR EACH MISCONDUCT TYPE)
# Only for respondents who answered "Yes" to Q4
# ================================================================

# 1. Filter respondents aware of misconduct
df_q4_yes = df[df["q04_label"] == "Yes"]

# 2. Titles for Q5 items
titles_q5 = {
    'q0501': 'Misreporting hours worked',
    'q0502': 'Safety violations',
    'q0503': 'Discrimination',
    'q0504': 'Stealing',
    'q0505': 'Improper hiring (nepotism)',
    'q0506': 'Fraud',
    'q0507': 'Bullying / Harassment',
    'q0508': 'Data misuse / Privacy breach',
    'q0509': 'Bribery / Corruption',
    'q0510': 'Environmental violations',
    'q0511': 'Abuse of authority',
    'q0512': 'Misuse of AI / Technology',
    'q0513': 'Other',
    'q0514': 'Prefer not to say'
}

q5_cols = list(titles_q5.keys())

# 3. Map 0/1 to No/Yes
yes_no_map = {0: "No", 1: "Yes"}
df_q5 = df_q4_yes[q5_cols].applymap(lambda x: yes_no_map.get(x, x))

# 4. Plotting grid
num_plots = len(q5_cols)
rows = 4
cols = 4

fig, axes = plt.subplots(rows, cols, figsize=(18, 16))
axes = axes.flatten()

total = len(df_q4_yes)

for i, col in enumerate(q5_cols):
    ax = axes[i]
    sns.countplot(
        x=col,
        data=df_q5,
        palette='Set2',
        order=["No", "Yes"],
        ax=ax
    )

    # Add counts & percentages
    for p in ax.patches:
        count = p.get_height()
        percent = (count / total) * 100
        ax.text(
            p.get_x() + p.get_width() / 2,
            count + 1,
            f"{count}\n({percent:.1f}%)",
            ha='center',
            va='bottom',
            fontsize=9,
            fontweight='bold'
        )

    ax.set_title(titles_q5[col], fontsize=12, fontweight='bold')
    ax.set_xlabel("")
    ax.set_ylabel("Count")
    ax.set_ylim(0, df_q5[col].value_counts().max() + 10)

# Remove any unused subplots
for j in range(num_plots, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()
```

**Text output:**

```text
<Figure size 1800x1600 with 14 Axes>
```

## Cell 112 — raw

```python
Q5 Insights — Types of Misconduct Observed (Among Those Who Answered “Yes” to Q4)

(Total respondents aware of misconduct: 114)

Your plots show the following approximate “Yes” counts & percentages:

Misconduct Type	Yes Count	% of Misconduct Observers
Bullying / Harassment	45	~39.5%
Data misuse / Privacy breach	24	~21.1%
Discrimination	29	~25.4%
Improper hiring / nepotism	21	~18.4%
Safety violations	41	~36%
Abuse of authority	35	~30.7%
Misreporting hours worked	27	~23.7%
Stealing	19	~16.7%
Fraud	10	~8.8%
Environmental violations	8	~7%
Misuse of AI / Tech	5	~4.4%
Bribery / Corruption	16	~14%
Other / Prefer not to say	6–10	~7–9%

(Percentages match visual labels)

🎯 1. Bullying / Harassment is the Most Frequently Observed Misconduct (~40%)

This is a significant red flag.

Implications:

Indicates cultural or leadership failures

Shows breakdown in interpersonal norms and psychological safety

Suggests that anti-bullying frameworks may be ineffective

Typically correlates with lower employee morale and trust

In ethical climate research, bullying/harassment is often considered a primary indicator of a weak ethical culture.

🎯 2. Safety Violations Also Very High (~36%)

This is alarming because safety misconduct jeopardises:

Physical well-being

Legal compliance

Organisational liability

A high percentage suggests:

Insufficient safety controls

Poor enforcement

Potential undertraining or operational pressure

This insight can be strongly tied to organisational responsibilities during Covid-19, where safety expectations increased.

🎯 3. Discrimination and Abuse of Authority Show Systemic Cultural Problems

Discrimination (~25%)

Abuse of authority (~31%)

These reflect deeper structural and hierarchical issues, not one-off events.

Patterns of authority misuse often arise in workplaces where:

Power imbalances are unchecked

Whistleblowing mechanisms are weak

Leadership ethics are inconsistent

Link this to Q11 (line manager ethics) in your multivariate analysis later:
→ Expect strong negative correlation.

🎯 4. Data Misuse / Privacy Breaches (21%) Signal Emerging Digital-Ethical Risks

Given increasing digitisation, this is very important.

Possible causes:

Weak data governance

Poor employee training

Pressure to meet productivity targets

Lack of cybersecurity awareness

This connects directly to Q15 (future ethical concerns) — you will likely see alignment.

🎯 5. Nepotism, Stealing, and Bribery Indicate “Everyday Unethical Practices”

Nepotism: 18%

Stealing: 17%

Bribery/corruption: 14%

These behaviours often:

Become normalised in weak ethical climates

Are invisible to senior management

Occur in isolated teams or units

This cluster suggests endemic integrity issues beyond just operational misconduct.

🎯 6. Fraud, Environmental Violations, Misuse of AI Are Less Common (<10%)

Lower frequency does not mean low risk.

Fraud and environmental violations typically:

Occur at higher organisational levels

Are harder for employees to detect

Require specialised knowledge to identify

Misuse of AI is emerging — low detection could reflect lack of awareness rather than absence.

🎯 7. “Prefer Not to Say” Responses (7–9%) Reflect Fear or Sensitivity

This is an incredibly important analytical insight.

Employees may avoid disclosure due to:

Fear of retaliation

Low confidence in anonymity

Fear of being associated with reporting behaviour

Emotional discomfort

This reinforces ethical climate weaknesses and survey bias.

🎯 8. Overall Pattern: Misconduct Is Multi-Dimensional, Not Isolated

The high counts across multiple categories indicate that:

Respondents often observe more than one type of misconduct

Issues span behaviour, safety, fairness, data, and ethics

Organisational culture may be fragmented

In a 90+ assignment, articulate that:

“Misconduct is not concentrated in a single domain but distributed across behavioural, procedural, and digital dimensions, highlighting the need for holistic ethical interventions.”

🎯 9. This Sets Up Perfectly for Q6–Q9 Reporting Behaviour Analysis

Q5 results give the foundation for:

Q6: Did they report the misconduct?

Q7: Were they satisfied?

Q8: Did they face retaliation?

Q9: Why did others not report?

This sequence builds a strong ethical narrative.

🎓 10. High-Scoring Interpretation Paragraph (Copy-Paste for Assignment)

“Among respondents aware of misconduct, bullying and harassment (39.5%) and safety violations (36%) emerge as the most prevalent issues, indicating significant weaknesses in interpersonal conduct and operational oversight. Discrimination (25.4%) and abuse of authority (30.7%) point to deeper cultural and hierarchical problems within the organisation. Data misuse (21.1%) highlights emerging digital ethics risks, particularly relevant in increasingly technology-driven environments. Lower-frequency behaviours such as fraud and environmental violations (<10%) may reflect limited visibility rather than absence. The presence of ‘Prefer not to say’ responses suggests discomfort and potential fear around ethical disclosure. Overall, the diversity and frequency of misconduct types observed indicate that ethical breaches are multi-dimensional rather than isolated incidents, underscoring the need for comprehensive ethical and managerial reforms.”
```

## Cell 114 — markdown

#### Q6. Did you raise or speak up about any of your concerns with management, another appropriate person, or through any other mechanism?

## Cell 115 — code

```python
# ================================================================
# Q6 ANALYSIS:
# "Did you raise or speak up about your concerns?"
# Only analyse respondents who answered "Yes" to Q4
# ================================================================

# 1. Filter respondents who observed misconduct (Q4 = Yes)
df_q4_yes = df[df["q04_label"] == "Yes"]

# 2. Map Q6 responses
q6_mapping = {
    1: "Yes",
    2: "No",
    3: "Prefer not to say"
}

df_q4_yes["q06_label"] = df_q4_yes["q06"].map(q6_mapping)

# 3. Frequency & percentage table
q6_freq = df_q4_yes["q06_label"].value_counts(dropna=False).reindex(q6_mapping.values())
q6_percent = (df_q4_yes["q06_label"].value_counts(normalize=True, dropna=False)
               .reindex(q6_mapping.values()) * 100).round(2)

q6_summary = pd.DataFrame({
    "Count": q6_freq,
    "Percentage": q6_percent
})

print("\n============== Q6 SUMMARY TABLE (Q4 = YES ONLY) ==============\n")
display(q6_summary)

# 4. Plot bar chart
plt.figure(figsize=(7,5))
q6_freq.plot(kind="bar", color="#4C72B0")

plt.title("Q6: Did You Report the Misconduct? (Among Those Aware)")
plt.xlabel("Response Options")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# ================================================================
# END OF Q6 ANALYSIS
# ================================================================
```

**Text output:**

```text
============== Q6 SUMMARY TABLE (Q4 = YES ONLY) ==============
```

```text
Count  Percentage
q06_label                           
Yes                   61       53.51
No                    49       42.98
Prefer not to say      4        3.51
```

```text
<Figure size 700x500 with 1 Axes>
```

## Cell 116 — raw

```python
'''''' Hint for Bivariate Anlaysis
4. Link Q6 back to Q5

For 90+ marks, interpret cross-links:

People who saw bullying/harassment are less likely to report

Those who observed fraud or bribery may fear severe consequences

Reporting rates tend to be low when power abuse is common

Later I can help you run:

df_q4_yes.groupby("q06_label")[q5_cols].mean() '''''''

“Of those who observed misconduct, 53.5% reported the issue, indicating a moderately strong ethical voice climate. However, the 43% who chose not to report highlight substantial cultural and structural barriers to escalation. This finding is particularly concerning given the high prevalence of bullying, harassment, safety violations and abuse of authority previously identified in Q5. The presence of ‘Prefer not to say’ responses further suggests psychological safety issues and a potential fear of retaliation. Overall, the reporting behaviour reflects a fragmented ethical culture in which reporting mechanisms function for some employees but fail to provide consistent trust and protection across the organisation.”

Note ::: Make Flow chart to show these connection between the questions
```

## Cell 117 — markdown

### outcome of unethical behaviour reporting

## Cell 118 — markdown

#### Q7. After raising or speaking up about your concerns, how satisfied or dissatisfied were you with the outcome?

## Cell 119 — code

```python
# ================================================================
# Q7 ANALYSIS:
# "After raising or speaking up about your concerns, how satisfied 
# or dissatisfied were you with the outcome?"
#
# Analyze ONLY respondents who:
#   1. Observed misconduct (Q4 = Yes)
#   2. Reported it (Q6 = Yes)
# ================================================================


# 1. Subset respondents who observed & reported misconduct
df_q6_yes = df_q4_yes[df_q4_yes["q06_label"] == "Yes"]

print("Number of respondents who reported misconduct:", len(df_q6_yes))

# 2. Q7 response mapping
q7_mapping = {
    1: "Very satisfied",
    2: "Fairly satisfied",
    3: "Fairly dissatisfied",
    4: "Very dissatisfied",
    5: "Don't know"
}

# 3. Apply mapping
df_q6_yes["q07_label"] = df_q6_yes["q07"].map(q7_mapping)

# 4. Frequency and percentage table
q7_freq = df_q6_yes["q07_label"].value_counts(dropna=False).reindex(q7_mapping.values())
q7_percent = (
    df_q6_yes["q07_label"]
    .value_counts(normalize=True, dropna=False)
    .reindex(q7_mapping.values()) * 100
).round(2)

q7_summary = pd.DataFrame({
    "Count": q7_freq,
    "Percentage": q7_percent
})

print("\n============== Q7 SUMMARY TABLE (Among Those Who Reported Misconduct) ==============\n")
display(q7_summary)

# 5. Bar chart
plt.figure(figsize=(9,5))
q7_freq.plot(kind="bar", color="#4C72B0")

plt.title("Q7: Satisfaction With Outcome After Reporting Misconduct")
plt.xlabel("Response Options")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# ================================================================
# END OF Q7 ANALYSIS
# ================================================================
```

**Text output:**

```text
Number of respondents who reported misconduct: 61

============== Q7 SUMMARY TABLE (Among Those Who Reported Misconduct) ==============
```

```text
Count  Percentage
q07_label                             
Very satisfied        17.0       27.87
Fairly satisfied      22.0       36.07
Fairly dissatisfied    9.0       14.75
Very dissatisfied     13.0       21.31
Don't know             NaN         NaN
```

```text
<Figure size 900x500 with 1 Axes>
```

## Cell 120 — raw

```python
## hint : Dissatisfaction likely correlates with certain misconduct types (from Q5) for birvariate 


“Among employees who reported misconduct, satisfaction with the outcome was mixed. While 63.9% expressed some level of satisfaction, a substantial 36% reported dissatisfaction, including 21.3% who were ‘very dissatisfied’. This indicates that although reporting mechanisms exist, their effectiveness is inconsistent and may not inspire confidence. The polarisation between ‘very satisfied’ and ‘very dissatisfied’ responses suggests that outcomes vary widely depending on the nature of the misconduct or the parties involved. The absence of ‘don’t know’ responses indicates procedural clarity, but the high dissatisfaction rate highlights deeper weaknesses in how cases are resolved. These findings help explain why 43% of employees chose not to report misconduct in Q6 and reflect a potentially fragile ethical climate""
```

## Cell 121 — markdown

#### Q8. After raising or speaking up about your concerns, did you experience any personal disadvantage or any form of retaliation for doing so?

## Cell 122 — code

```python
# ================================================================
# Q8 ANALYSIS:
# "After raising your concerns, did you experience any personal 
# disadvantage or retaliation?"
#
# Analyze ONLY respondents who:
#   1. Observed misconduct (Q4 = Yes)
#   2. Reported it (Q6 = Yes)
# ================================================================

# 1. Subset respondents who reported misconduct
df_q6_yes = df_q4_yes[df_q4_yes["q06_label"] == "Yes"]

print("Number of respondents who reported misconduct:", len(df_q6_yes))

# 2. Q8 response mapping
q8_mapping = {
    1: "Yes",
    2: "No",
    3: "Prefer not to say"
}

# 3. Apply mapping
df_q6_yes["q08_label"] = df_q6_yes["q08"].map(q8_mapping)

# 4. Frequency & percentage table
q8_freq = df_q6_yes["q08_label"].value_counts(dropna=False).reindex(q8_mapping.values())
q8_percent = (
    df_q6_yes["q08_label"]
    .value_counts(normalize=True, dropna=False)
    .reindex(q8_mapping.values()) * 100
).round(2)

q8_summary = pd.DataFrame({
    "Count": q8_freq,
    "Percentage": q8_percent
})

print("\n============== Q8 SUMMARY TABLE (Among Those Who Reported Misconduct) ==============\n")
display(q8_summary)

# 5. Bar chart
plt.figure(figsize=(8,5))
q8_freq.plot(kind="bar", color="#4C72B0")

plt.title("Q8: Experienced Retaliation After Reporting Misconduct")
plt.xlabel("Response Options")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# ================================================================
# END OF Q8 ANALYSIS
# ================================================================
```

**Text output:**

```text
Number of respondents who reported misconduct: 61

============== Q8 SUMMARY TABLE (Among Those Who Reported Misconduct) ==============
```

```text
Count  Percentage
q08_label                           
Yes                   30       49.18
No                    29       47.54
Prefer not to say      2        3.28
```

```text
<Figure size 800x500 with 1 Axes>
```

## Cell 123 — raw

```python
“Among employees who reported misconduct, 49.2% experienced retaliation or personal disadvantage, indicating a severe breakdown in psychological safety and ethical governance. This rate is substantially higher than typical organisational benchmarks and suggests that whistleblowing mechanisms, although present, are ineffective in protecting those who speak up. The near-equal split between retaliation and non-retaliation reflects highly inconsistent managerial responses, which can undermine organisational trust and foster a culture of fear. These findings help explain the high non-reporting rate observed in Q6, as employees may learn through observation or experience that speaking up carries significant personal risk. The presence of ‘Prefer not to say’ responses further underscores the sensitivity of the issue and the potential fear associated with admitting retaliation.
```

## Cell 124 — markdown

#### Q9. Which of the following, if any, influenced your decision not to raise or speak up about your concerns? 
##### I felt it was none of my business
##### I felt I might jeopardise my job
##### I did not believe that corrective action would be taken
##### I did not want to be seen as a troublemaker by management
##### I did not know who to contact
##### I thought that it was common practice
##### I thought it would be raised by someone else
##### I thought that they already knew about it
##### I didn't think it was a serious issue at the time
##### Other
##### Prefer not to say

## Cell 125 — code

```python
q9_titles = {
    "q0901": "None of my business",
    "q0902": "Might jeopardise my job",
    "q0903": "No corrective action expected",
    "q0904": "Fear of alienation",
    "q0905": "Fear of being seen as troublemaker",
    "q0906": "Did not know who to contact",
    "q0907": "Thought it was common practice",
    "q0908": "Thought someone else would raise it",
    "q0909": "Thought they already knew",
    "q0910": "Didn't think it was serious",
    "q0911": "Other",
    "q0912": "Prefer not to say"
}
q9_cols = list(q9_titles.keys())
df_q9 = df_q4_yes[df_q4_yes["q06_label"] == "No"]
print("Number of respondents who stayed silent:", len(df_q9))
yes_no_map = {0: "No", 1: "Yes"}
df_q9_mapped = df_q9[q9_cols].applymap(lambda x: yes_no_map.get(x, x))

num_plots = len(q9_cols)
rows = 4
cols = 3  # 12 items → 4x3 grid

fig, axes = plt.subplots(rows, cols, figsize=(18, 16))
axes = axes.flatten()

total = len(df_q9)

for i, col in enumerate(q9_cols):
    ax = axes[i]
    sns.countplot(
        x=col,
        data=df_q9_mapped,
        palette="Set2",
        order=["No", "Yes"],
        ax=ax
    )

    # Add counts + percentages
    for p in ax.patches:
        count = p.get_height()
        percent = (count / total) * 100 if total > 0 else 0
        ax.text(
            p.get_x() + p.get_width()/2,
            count + 0.5,
            f"{count}\n({percent:.1f}%)",
            ha="center", va="bottom",
            fontsize=9, fontweight="bold"
        )

    ax.set_title(q9_titles[col], fontsize=12, fontweight="bold")
    ax.set_xlabel("")
    ax.set_ylabel("Count")
    ax.set_ylim(0, max(df_q9_mapped[col].value_counts()) + 5)

# Remove unused axes if any
for j in range(num_plots, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()
```

**Text output:**

```text
Number of respondents who stayed silent: 49
```

```text
<Figure size 1800x1600 with 12 Axes>
```

## Cell 126 — raw

```python
“Among employees who observed misconduct but did not report it, the dominant barrier to speaking up was a lack of confidence in organisational action, with 61.2% believing that no corrective response would occur. This highlights a systemic trust deficit in ethical governance. Fear-based barriers were also prominent, with 30.6% concerned about job jeopardy and an equal proportion fearing being labelled a troublemaker, complemented by 22.4% who feared alienation from colleagues. These concerns are validated by the high retaliation rate observed in Q8 (49%). Knowledge barriers were minimal, suggesting that awareness of reporting channels exists, but credibility and psychological safety are lacking. The low frequency of reasons such as ‘did not think it was serious’ indicates that most unreported misconduct involved issues perceived as serious by employees. Overall, Q9 reveals a workplace environment where silence is driven not by uncertainty or triviality but by a rational fear of personal consequences and a profound distrust in organisational responsiveness.”
```

## Cell 128 — markdown

#### Q10. My organisation has 
##### "q1001": "Written ethical standards (code of ethics)",
##### "q1002": "Confidential reporting channels",
##### "q1003": "Ethics advice helpline available",
##### "q1004": "Ethics training provided",
##### "q1005": "AI ethics guidelines provided"

## Cell 130 — code

```python
# ================================================================
# Q10 ANALYSIS (Organisational Support for Ethics)
# Categories: 1 = Yes, 2 = No, 3 = Don't know
# ================================================================
# -----------------------------------------
# 1. Titles for Q10 items
# -----------------------------------------
q10_titles = {
    "q10_01": "Written ethical standards (Code of ethics)",
    "q10_02": "Confidential misconduct reporting",
    "q10_03": "Ethics advice helpline available",
    "q10_04": "Ethics training provided",
    "q10_05": "AI ethics guidelines available"
}

q10_cols = [col for col in df.columns if col.startswith("q10")]

#print(q10_cols)

# -----------------------------------------
# 2. Mapping values to labels
# -----------------------------------------
q10_map = {
    1: "Yes",
    2: "No",
    3: "Don't know"
}

df_q10 = df[q10_cols].applymap(lambda x: q10_map.get(x, x))

# -----------------------------------------
# 3. Plotting setup
# -----------------------------------------
num_items = len(q10_cols)
rows = 2
cols = 3  # Good for 5 items

fig, axes = plt.subplots(rows, cols, figsize=(16, 10))
axes = axes.flatten()

total = len(df)
order = ["Yes", "No", "Don't know"]

for i, col in enumerate(q10_cols):
    ax = axes[i]
    sns.countplot(
        x=col,
        data=df_q10,
        palette="Set2",
        order=order,
        ax=ax
    )

    # Add counts and percentages
    for p in ax.patches:
        count = p.get_height()
        percent = (count / total) * 100
        ax.text(
            p.get_x() + p.get_width()/2,
            count + 1,
            f"{count}\n({percent:.1f}%)",
            ha="center",
            fontsize=9,
            fontweight="bold"
        )

    ax.set_title(q10_titles[col], fontsize=12, fontweight="bold")
    ax.set_xlabel("")
    ax.set_ylabel("Count")
    ax.set_ylim(0, df_q10[col].value_counts().max() + 10)

# Delete unused axis
for j in range(num_items, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()
```

**Text output:**

```text
<Figure size 1600x1000 with 4 Axes>
```

## Cell 131 — raw

```python
“Q10 assesses the organisation’s ethical infrastructure, revealing mixed levels of support. While approximately 70% of respondents confirmed the presence of written ethical standards, awareness and utilisation of other mechanisms were notably weaker. Only 61% acknowledged having confidential reporting channels, and around half reported access to ethics advice helplines or formal ethics training. Across all items, 12–18% selected ‘Don’t know,’ indicating significant communication gaps. These findings suggest that although ethical structures exist, they are inconsistently communicated and insufficiently embedded in the organisational culture. This may help explain the high levels of non-reporting (Q6), scepticism about corrective action (Q9), and substantial retaliation experiences (Q8).”
```

## Cell 132 — markdown

### Perception of manager and organization on ethics

## Cell 134 — code

```python
# ================================================================
# Q11 ANALYSIS (Perception of Manager & Organisation Ethics)
# Likert scale (1–6)
# ================================================================
# -----------------------------------------
# 1. Titles for Q11 items
# -----------------------------------------
q11_titles = {
    "q11_01": "Line manager sets good ethical example",
    "q11_02": "Line manager explains importance of ethics",
    "q11_03": "Line manager rewards unethical behaviour",
    "q11_04": "Line manager supports me in ethical behaviour",
    "q11_05": "Organisation disciplines unethical behaviour",
    "q11_06": "Organisation acts responsibly in business dealings",
    "q11_07": "Organisation lives up to social responsibility",
    "q11_08": "Right & wrong discussed in staff meetings",
    "q11_09": "Line management show honest behaviour",
    "q11_10": "Senior management take ethics seriously",
    "q11_11": "Decisions about people are fair",
    "q11_12": "People know expected ethical behaviour",
    "q11_13": "People talk about right and wrong",
    "q11_14": "People held accountable when breaking rules"
}

q11_cols = list(q11_titles.keys())

# -----------------------------------------
# 2. Mapping values to labels
# -----------------------------------------
q11_map = {
    1: "Strongly agree",
    2: "Tend to agree",
    3: "Neither nor",
    4: "Tend to disagree",
    5: "Strongly disagree",
    6: "Prefer not to say"
}

df_q11 = df[q11_cols].applymap(lambda x: q11_map.get(x, x))

# -----------------------------------------
# 3. Category order for consistent Likert charts
# -----------------------------------------
likert_order = [
    "Strongly agree",
    "Tend to agree",
    "Neither nor",
    "Tend to disagree",
    "Strongly disagree",
    "Prefer not to say"
]

# -----------------------------------------
# 4. Plotting each Q11 item (Horizontal bars)
# -----------------------------------------
rows = 7
cols = 2  # 14 items → 7 x 2 grid

fig, axes = plt.subplots(rows, cols, figsize=(18, 28))
axes = axes.flatten()

for i, col in enumerate(q11_cols):
    ax = axes[i]
    freq = df_q11[col].value_counts().reindex(likert_order)

    sns.barplot(
        y=freq.index,
        x=freq.values,
        palette="viridis",
        ax=ax
    )

    # Title
    ax.set_title(q11_titles[col], fontsize=12, fontweight="bold")

    # Add counts
    for index, value in enumerate(freq.values):
        ax.text(value + 2, index, f"{value}", va="center", fontsize=9)

    ax.set_xlabel("Count")
    ax.set_ylabel("Response")

# Remove empty axes
for j in range(len(q11_cols), len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()
```

**Text output:**

```text
<Figure size 1800x2800 with 14 Axes>
```

## Cell 135 — raw

```python
“The Q11 results indicate a generally positive but uneven ethical climate. Line managers are widely perceived as ethical role models, with strong agreement that they set good examples, communicate expectations, and support ethical behaviour. Organisational-level ethics also receive majority support, particularly in social responsibility and responsible dealings with external stakeholders. However, several areas highlight structural weaknesses, including inconsistent disciplinary action, perceived unfairness in people decisions, and limited discussion of ethical issues in everyday work practices. A noteworthy minority believe that managers reward unethical behaviour, signalling pockets of unethical leadership. High neutrality across many items further suggests ambiguity or inconsistent visibility of ethical norms. Collectively, these findings portray an organisation with ethical frameworks in place but variable implementation, aligning with earlier observations about distrust in corrective action (Q9) and high retaliation experiences (Q8).”
```

## Cell 136 — markdown

### Q12. Have you felt pressured to compromise your current organisation's standards of ethical conduct?

## Cell 137 — code

```python
# ================================================================
# Q12 ANALYSIS WITH PIE CHART
# "Have you felt pressured to compromise ethical standards?"
# ================================================================


# 1. Mapping dictionary
q12_map = {
    1: "Yes",
    2: "No",
    3: "Prefer not to say"
}

# 2. Map values
df["q12_label"] = df["q12"].map(q12_map)

# 3. Summary table
q12_counts = df["q12_label"].value_counts(dropna=False)
q12_percent = (q12_counts / len(df) * 100).round(2)

q12_summary = pd.DataFrame({
    "Count": q12_counts,
    "Percentage": q12_percent
})

print("\n============== Q12 SUMMARY TABLE ==============\n")
display(q12_summary)

# 4. Pie Chart
plt.figure(figsize=(7,7))
plt.pie(
    q12_counts,
    labels=q12_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#66c2a5", "#fc8d62", "#8da0cb"],
    textprops={"fontsize": 12, "weight": "bold"}
)

plt.title("Q12: Pressured to Compromise Ethical Standards", fontsize=14, fontweight="bold")
plt.show()
```

**Text output:**

```text
============== Q12 SUMMARY TABLE ==============
```

```text
Count  Percentage
q12_label                           
No                   578       86.66
Yes                   74       11.09
Prefer not to say     15        2.25
```

```text
<Figure size 700x700 with 1 Axes>
```

## Cell 138 — raw

```python
“Most employees (86.7%) reported no pressure to compromise ethical standards, indicating that direct coercion into unethical conduct is not widespread within the organisation. However, the 11.1% who did experience such pressure represent a meaningful minority whose experiences merit closer examination in Q13. The presence of ‘Prefer not to say’ responses (2.25%) also suggests some sensitivity or fear associated with this item, consistent with earlier findings on retaliation (Q8). While direct pressure appears low, wider organisational factors—such as inconsistent accountability (Q11), doubts about corrective action (Q9), and high retaliation rates—may indirectly contribute to ethical compromise even in the absence of overt pressure.”
```

## Cell 139 — code

```python
df.head()
```

**Text output:**

```text
serial  sq1  d01  d02_group  d04  d05  d08a  d08b  d08c01  d08c02  d08c03  d08c04  d08c05  d08c06  d08c07  d08c08  d08c09  d08c10  d08c11  d08c12  d09  d10  q01_01  q01_02  q01_03  q01_04  q01_05  q01_06  q01_07  q01_08  q02  q03  q04  q0501  q0502  q0503  q0504  q0505  q0506  q0507  q0508  q0509  q0510  q0511  q0512  q0513  q0514  q06  q07  q08  q0901  q0902  q0903  q0904  q0905  q0906  q0907  q0908  q0909  q0910  q0911  q0912  q10_01  q10_02  q10_03  q10_04  q11_01  q11_02  q11_03  q11_04  q11_05  q11_06  q11_07  q11_08  q11_09  q11_10  q11_11  q11_12  q11_13  q11_14  q12  q1301  q1302  q1303  q1304  q1305  q1306  q1307  q1308  q1309  q1310  q1311  q1312  q14_01  q14_02  q14_03  q14_04  q14_05  q15_01  q15_02  q15_03  q15_04  q15_05  q15_06  q15_07  q15_08  q15_09 gender_labeled age_group_labeled                 sector_label     d05_labeled d08a_label d08b_label               q03_label AI_Adoption AI_Interaction   q02_label q04_label q12_label
0      35    2    1          2    7    2     1     2       0       0       0       0       0       0       0       1       0       0       0       0    2    2       2       1       3       4       4       3       3       3    1    1    1    1.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0  1.0  4.0  2.0    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN       1       1       1       1       1       1       3       1       1       2       1       1       1       2       1       1       1       2    2    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN       2       1       1       2       5       1       4       1       1       1       2       2       1       1           Male             25–34          Finance & Insurance  Private Sector        Yes         No  Significantly improved          No             No      Always       Yes        No
1      59    2    2          2   11    1     1     1       1       0       0       0       1       0       0       1       0       0       0       0    1    1       4       3       4       4       4       1       2       4    1    1    1    1.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0  1.0  1.0  1.0    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN       1       1       1       1       2       1       1       1       1       1       1       2       1       1       1       2       1       1    1    0.0    0.0    0.0    1.0    0.0    0.0    0.0    0.0    1.0    0.0    0.0    0.0       1       1       1       1       1       2       2       1       2       2       4       2       2       2         Female             25–34  Information & Communication   Public Sector        Yes        Yes  Significantly improved         Yes            Yes      Always       Yes       Yes
2      86    2    2          4   11    2     1     2       1       0       0       0       1       0       0      
... [output truncated]
```

## Cell 140 — markdown

### Pressures to act unethically

## Cell 141 — markdown

#### Q13. Which of the following, if any, were the main pressures on you to act unethically?

## Cell 142 — code

```python
# ================================================================
# Q13 SUMMARY TABLE + PIE CHARTS for respondents who said YES in Q12
# ================================================================
# Filter only Q12 = Yes respondents
df_q12_yes = df[df["q12"] == 1].copy()
n_q12_yes = len(df_q12_yes)
print("Number of respondents who felt pressured (Q12 = Yes):", n_q12_yes)

# Q13 columns
q13_cols = [
    "q1301", "q1302", "q1303", "q1304",
    "q1305", "q1306", "q1307", "q1308",
    "q1309", "q1310", "q1311", "q1312"
]

q13_titles = {
    "q1301": "Unrealistic business objectives",
    "q1302": "Following boss's orders",
    "q1303": "Peer pressure to be a team player",
    "q1304": "Help organisation perform better",
    "q1305": "Trying to save my job",
    "q1306": "Unethical organisational culture",
    "q1307": "Asked to take shortcuts",
    "q1308": "Financial/budget pressure",
    "q1309": "Under-resourced",
    "q1310": "Time pressure / unrealistic deadlines",
    "q1311": "Other",
    "q1312": "Prefer not to say"
}

# Function to count Yes / No / Prefer not to say
def q13_counts(series):
    vals = series
    yes = (vals == 1).sum()
    pns = (vals == 3).sum()
    no = len(vals) - yes - pns
    return pd.Series([yes, no, pns], index=["Yes", "No", "Prefer not to say"])

# ==============================
# ✔ 1. GENERATE SUMMARY TABLE
# ==============================
summary_rows = []

for col in q13_cols:
    counts = q13_counts(df_q12_yes[col])
    total = counts.sum()
    percentages = (counts / total * 100).round(2)

    for resp, count_value in counts.items():
        summary_rows.append({
            "Question": q13_titles[col],
            "Response": resp,
            "Count": count_value,
            "Percentage": percentages[resp]
        })

summary_df = pd.DataFrame(summary_rows)

print("\n=============== CLEAN Q13 SUMMARY TABLE ===============\n")
print(summary_df.to_string(index=False))

# ==============================
# ✔ 2. PIE CHARTS FOR ALL Q13 ITEMS
# ==============================

rows, cols = 4, 3
fig, axes = plt.subplots(rows, cols, figsize=(18, 18))
axes = axes.flatten()

colors = ["#66c2a5", "#fc8d62", "#8da0cb"]

for i, col in enumerate(q13_cols):
    ax = axes[i]
    counts = q13_counts(df_q12_yes[col])

    if counts.sum() == 0:
        ax.text(0.5, 0.5, "No responses", ha="center", va="center")
        ax.set_title(q13_titles[col], fontsize=12)
        ax.axis("off")
        continue

    ax.pie(
        counts.values,
        labels=counts.index,
        autopct="%1.1f%%",
        colors=colors,
        startangle=90
    )
    ax.set_title(q13_titles[col], fontsize=12)

plt.tight_layout()
plt.show()

# =============================
```

**Text output:**

```text
Number of respondents who felt pressured (Q12 = Yes): 74

=============== CLEAN Q13 SUMMARY TABLE ===============

                             Question          Response  Count  Percentage
      Unrealistic business objectives               Yes     19       25.68
      Unrealistic business objectives                No     55       74.32
      Unrealistic business objectives Prefer not to say      0        0.00
              Following boss's orders               Yes     17       22.97
              Following boss's orders                No     57       77.03
              Following boss's orders Prefer not to say      0        0.00
    Peer pressure to be a team player               Yes     11       14.86
    Peer pressure to be a team player                No     63       85.14
    Peer pressure to be a team player Prefer not to say      0        0.00
     Help organisation perform better               Yes     16       21.62
     Help organisation perform better                No     58       78.38
     Help organisation perform better Prefer not to say      0        0.00
                Trying to save my job               Yes     17       22.97
                Trying to save my job                No     57       77.03
                Trying to save my job Prefer not to say      0        0.00
     Unethical organisational culture               Yes     12       16.22
     Unethical organisational culture                No     62       83.78
     Unethical organisational culture Prefer not to say      0        0.00
              Asked to take shortcuts               Yes     23       31.08
              Asked to take shortcuts                No     51       68.92
              Asked to take shortcuts Prefer not to say      0        0.00
            Financial/budget pressure               Yes     18       24.32
            Financial/budget pressure                No     56       75.68
            Financial/budget pressure Prefer not to say      0        0.00
                      Under-resourced               Yes     16       21.62
                      Under-resourced                No     58       78.38
                      Under-resourced Prefer not to say      0        0.00
Time pressure / unrealistic deadlines               Yes     22       29.73
Time pressure / unrealistic deadlines                No     52       70.27
Time pressure / unrealistic deadlines Prefer not to say      0        0.00
                                Other               Yes      0        0.00
                                Other                No     74      100.00
                                Other Prefer not to say      0        0.00
                    Prefer not to say               Yes      2        2.70
                    Prefer not to say                No     72       97.30
                    Prefer not to say Prefer not to say      0        0.00
```

```text
<Figure size 1800x1800 with 12 Axes>
```

## Cell 143 — raw

```python
Although only 11% of employees reported feeling pressured to compromise ethical standards (Q12), the nature of this pressure provides important insight. The main drivers were operational demands — shortcuts (31%), unrealistic deadlines (30%), financial constraints (24%), and unrealistic targets (26%). Managerial pressure was less dominant but still significant, affecting around one in four employees. These patterns suggest that unethical behaviour is primarily shaped by organisational systems and workload expectations, rather than intentional misconduct or peer influence. When interpreted alongside Q11, which showed strong perceptions of ethical leadership, the evidence indicates that ethical risk is embedded more in structural performance pressures than in the ethical climate set by leaders.
```

## Cell 144 — markdown

#### To what extent do you agree or disagree with each of the following statements?
#####  Minor breaches of the rules are inevitable in a modern organisation
##### If we cracked down on every minor breach of the rules, we would soon find we had no staff 
##### If we cracked down on every minor breach of the rules, we would soon find we had no suppliers
#####  As long as I come in on time and within budget, I am not going to worry about some minor breaches of the rules
##### It is acceptable to artificially increase profits in the books as long as no money is stolen

## Cell 145 — code

```python
# ================================================================
# Q14 ANALYSIS – Likert Scale (5 statements)
# ================================================================
# Question titles
q14_titles = {
    "q14_01": "Minor breaches are inevitable",
    "q14_02": "Cracking down → no staff left",
    "q14_03": "Cracking down → no suppliers left",
    "q14_04": "Not worried about minor breaches if on time & budget",
    "q14_05": "Acceptable to inflate profits if no money stolen"
}

q14_cols = list(q14_titles.keys())

# Mapping Likert values
likert_map = {
    1: "Strongly agree",
    2: "Tend to agree",
    3: "Neither/nor",
    4: "Tend to disagree",
    5: "Strongly disagree",
    6: "Prefer not to say"
}

# Apply mapping
df_q14 = df[q14_cols].applymap(lambda x: likert_map.get(x, x))

# ================================================================
# 1. SUMMARY TABLE FOR Q14
# ================================================================

summary_list = []

for col in q14_cols:
    counts = df_q14[col].value_counts().reindex(likert_map.values()).fillna(0)
    percentages = (counts / counts.sum() * 100).round(2)
    
    for resp in counts.index:
        summary_list.append({
            "Question": q14_titles[col],
            "Response": resp,
            "Count": counts[resp],
            "Percentage": percentages[resp]
        })

summary_q14 = pd.DataFrame(summary_list)

print("\n=============== Q14 SUMMARY TABLE ===============\n")
print(summary_q14.to_string(index=False))


# ================================================================
# 2. HORIZONTAL BAR CHARTS FOR Q14
# ================================================================

# Order responses logically
likert_order = [
    "Strongly disagree",
    "Tend to disagree",
    "Neither/nor",
    "Tend to agree",
    "Strongly agree",
    "Prefer not to say"
]

# Plot setup
fig, axes = plt.subplots(3, 2, figsize=(18, 16))
axes = axes.flatten()

for i, col in enumerate(q14_cols):
    ax = axes[i]
    data = df_q14[col].value_counts().reindex(likert_order).fillna(0)
    
    sns.barplot(
        x=data.values,
        y=data.index,
        ax=ax,
        palette="viridis"
    )

    # Add value labels
    for j, val in enumerate(data.values):
        ax.text(val + 1, j, f"{int(val)}", va='center', fontsize=10)

    ax.set_title(q14_titles[col], fontsize=13, fontweight="bold")
    ax.set_xlabel("Count")
    ax.set_ylabel("Response")

# Remove the extra empty subplot if any
fig.delaxes(axes[-1])

plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Q14 SUMMARY TABLE ===============

                                            Question          Response  Count  Percentage
                       Minor breaches are inevitable    Strongly agree     63        9.45
                       Minor breaches are inevitable     Tend to agree    313       46.93
                       Minor breaches are inevitable       Neither/nor    147       22.04
                       Minor breaches are inevitable  Tend to disagree     94       14.09
                       Minor breaches are inevitable Strongly disagree     40        6.00
                       Minor breaches are inevitable Prefer not to say     10        1.50
                       Cracking down → no staff left    Strongly agree     85       12.74
                       Cracking down → no staff left     Tend to agree    217       32.53
                       Cracking down → no staff left       Neither/nor    147       22.04
                       Cracking down → no staff left  Tend to disagree    129       19.34
                       Cracking down → no staff left Strongly disagree     78       11.69
                       Cracking down → no staff left Prefer not to say     11        1.65
                   Cracking down → no suppliers left    Strongly agree     58        8.70
                   Cracking down → no suppliers left     Tend to agree    176       26.39
                   Cracking down → no suppliers left       Neither/nor    212       31.78
                   Cracking down → no suppliers left  Tend to disagree    121       18.14
                   Cracking down → no suppliers left Strongly disagree     85       12.74
                   Cracking down → no suppliers left Prefer not to say     15        2.25
Not worried about minor breaches if on time & budget    Strongly agree     45        6.75
Not worried about minor breaches if on time & budget     Tend to agree    165       24.74
Not worried about minor breaches if on time & budget       Neither/nor    188       28.19
Not worried about minor breaches if on time & budget  Tend to disagree    162       24.29
Not worried about minor breaches if on time & budget Strongly disagree     95       14.24
Not worried about minor breaches if on time & budget Prefer not to say     12        1.80
    Acceptable to inflate profits if no money stolen    Strongly agree     27        4.05
    Acceptable to inflate profits if no money stolen     Tend to agree     53        7.95
    Acceptable to inflate profits if no money stolen       Neither/nor     94       14.09
    Acceptable to inflate profits if no money stolen  Tend to disagree    165       24.74
    Acceptable to inflate profits if no money stolen Strongly disagree    315       47.23
    Acceptable to inflate profits if no money stolen Prefer not to say     13        1.95
```

```text
<Figure size 1800x1600 with 5 Axes>
```

## Cell 146 — raw

```python
Q14 reveals an important distinction in employees’ ethical reasoning. While most respondents perceive minor rule breaches as inevitable and, in some cases, necessary to navigate operational constraints, the overwhelming majority reject deliberate acts of financial manipulation. These findings suggest that employees operate within a “practical compliance” mindset—upholding core ethical principles while selectively bending lower-level rules to meet organisational demands. When viewed alongside Q13, which highlighted time pressure, unrealistic deadlines, and the need for shortcuts as key drivers of unethical pressure, the data paints a consistent picture of structural constraints shaping ethical behaviour more than individual dispositions. Overall, employees appear ethically grounded but constrained by operational realities.
```

## Cell 148 — markdown

#### How concerned, if at all, are you about the following issues with regards to the future of the workplace?
##### Misuse of Artificial Intelligence (AI) for unethical behaviour (e.g. discrimination, privacy violations ...) 
##### Automated machines or Artificial Intelligence replacing humans in the workplace -
##### Loss of interpersonal interactions due to new technologies 
##### Loss of interpersonal interactions due to the effects of the Covid-19 lockdown
##### Increased level of unethical behaviour due to an increase in the use of new technologies 
##### Inability of organisations to live up to their stated ethical standards
##### Discrimination or bias in the workplace 
##### Increased surveillance and monitoring in the workplace
##### New workplace/skillset requirements due to digitalisation and new technologies

## Cell 149 — code

```python
# ================================================================
# Q15 ANALYSIS – Concerns About the Ethical Future of Work
# Likert scale (1–6) for 9 items
# ================================================================


# -----------------------------------------
# 1. Q15 Titles
# -----------------------------------------
q15_titles = {
    "q15_01": "Misuse of AI for unethical behaviour",
    "q15_02": "AI replacing humans in the workplace",
    "q15_03": "Loss of interpersonal interactions (technology)",
    "q15_04": "Loss of interpersonal interactions (Covid-19 lockdown)",
    "q15_05": "Unethical behaviour increasing with new tech",
    "q15_06": "Organisations failing ethical standards",
    "q15_07": "Discrimination or bias in the workplace",
    "q15_08": "Increased workplace surveillance/monitoring",
    "q15_09": "New skillset requirements due to digitalisation"
}

q15_cols = list(q15_titles.keys())

# -----------------------------------------
# 2. Mapping dictionary
# -----------------------------------------
q15_map = {
    1: "Extremely concerned",
    2: "Moderately concerned",
    3: "Slightly concerned",
    4: "Not very concerned",
    5: "Not at all concerned",
    6: "Prefer not to say"
}

# Apply mapping
df_q15 = df[q15_cols].applymap(lambda x: q15_map.get(x, x))

# -----------------------------------------
# 3. Plotting – Horizontal bar plots (Likert)
# -----------------------------------------
fig, axes = plt.subplots(3, 3, figsize=(22, 18))
axes = axes.flatten()

likert_order = [
    "Extremely concerned",
    "Moderately concerned",
    "Slightly concerned",
    "Not very concerned",
    "Not at all concerned",
    "Prefer not to say"
]

for i, col in enumerate(q15_cols):
    ax = axes[i]
    counts = df_q15[col].value_counts().reindex(likert_order)

    sns.barplot(
        x=counts.values,
        y=counts.index,
        palette="viridis",
        ax=ax
    )

    # Annotate bars
    for idx, value in enumerate(counts.values):
        if not pd.isna(value):
            ax.text(value + 2, idx, str(value), va='center', fontsize=10)

    ax.set_title(q15_titles[col], fontsize=13, fontweight="bold")
    ax.set_xlabel("Count")
    ax.set_ylabel("Response")

# Remove extra axes if fewer than 9
for j in range(len(q15_cols), len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()

# -----------------------------------------
# 4. SUMMARY TABLE FOR Q15
# -----------------------------------------
summary_rows = []

for col in q15_cols:
    counts = df_q15[col].value_counts().reindex(likert_order)
    total = counts.sum()
    percentages = (counts / total * 100).round(2)

    for resp, count_value in counts.items():
        summary_rows.append({
            "Question": q15_titles[col],
            "Response": resp,
            "Count": count_value,
            "Percentage": percentages[resp]
        })

summary_q15 = pd.DataFrame(summary_rows)

print("\n=============== Q15 SUMMARY TABLE ===============\n")
print(summary_q15.to_string(index=False))
```

**Text output:**

```text
<Figure size 2200x1800 with 9 Axes>
```

```text
=============== Q15 SUMMARY TABLE ===============

                                              Question             Response  Count  Percentage
                  Misuse of AI for unethical behaviour  Extremely concerned     93       13.94
                  Misuse of AI for unethical behaviour Moderately concerned    132       19.79
                  Misuse of AI for unethical behaviour   Slightly concerned    155       23.24
                  Misuse of AI for unethical behaviour   Not very concerned    164       24.59
                  Misuse of AI for unethical behaviour Not at all concerned     98       14.69
                  Misuse of AI for unethical behaviour    Prefer not to say     25        3.75
                  AI replacing humans in the workplace  Extremely concerned     86       12.89
                  AI replacing humans in the workplace Moderately concerned    146       21.89
                  AI replacing humans in the workplace   Slightly concerned    150       22.49
                  AI replacing humans in the workplace   Not very concerned    167       25.04
                  AI replacing humans in the workplace Not at all concerned     96       14.39
                  AI replacing humans in the workplace    Prefer not to say     22        3.30
       Loss of interpersonal interactions (technology)  Extremely concerned     67       10.04
       Loss of interpersonal interactions (technology) Moderately concerned    167       25.04
       Loss of interpersonal interactions (technology)   Slightly concerned    172       25.79
       Loss of interpersonal interactions (technology)   Not very concerned    166       24.89
       Loss of interpersonal interactions (technology) Not at all concerned     77       11.54
       Loss of interpersonal interactions (technology)    Prefer not to say     18        2.70
Loss of interpersonal interactions (Covid-19 lockdown)  Extremely concerned     99       14.84
Loss of interpersonal interactions (Covid-19 lockdown) Moderately concerned    195       29.24
Loss of interpersonal interactions (Covid-19 lockdown)   Slightly concerned    152       22.79
Loss of interpersonal interactions (Covid-19 lockdown)   Not very concerned    134       20.09
Loss of interpersonal interactions (Covid-19 lockdown) Not at all concerned     67       10.04
Loss of interpersonal interactions (Covid-19 lockdown)    Prefer not to say     20        3.00
          Unethical behaviour increasing with new tech  Extremely concerned     60        9.00
          Unethical behaviour increasing with new tech Moderately concerned    126       18.89
          Unethical behaviour increasing with new tech   Slightly concerned    146       21.89
          Unethical behaviour increasing with new tech   Not very concerned    231       34.63
          Unethical behaviour increasing with new tech Not at all concerned     81       12.14
          Unethical behaviour increasing with new tech    Prefer not to say     23        3.45
    
... [output truncated]
```

## Cell 150 — raw

```python
The Q15 results show that employees are moderately concerned about the ethical implications of AI and digitalisation but do not perceive them as severe threats. Concerns are highest around AI misuse, workplace surveillance, and the erosion of interpersonal interaction—issues that directly affect trust, fairness, and autonomy at work. In contrast, employees show relatively low concern about unethical behaviour being caused by new technologies and only moderate concern about automation-related job loss. These patterns suggest that employees believe ethical risks stem more from organisational decisions and governance than from technology itself. Combined with the insights from Q11–Q13, the data indicates a workplace where structural pressures—rather than AI systems—pose the greatest threat to ethical behaviour.
```

## Cell 151 — markdown

## 5b Index Calculation for Bivariate Analysis

## Cell 152 — markdown

### now for Bivariate Analysis, We will calculate some index for likert Items

## Cell 153 — markdown

### Ethical Acceptability Index (EAI)
q01_01, q01_02, q01_03, q01_04, q01_05, q01_06, q01_07, q01_08

## Cell 154 — code

```python
# Define Q1 columns related to ethical acceptability
q1_cols = ['q01_01', 'q01_02', 'q01_03', 'q01_04',
           'q01_05', 'q01_06', 'q01_07', 'q01_08']

# Recode mapping: higher number = more accepting of unethical behavior
acceptability_map = {
    1: 5,  # Totally acceptable
    2: 4,  # Fairly acceptable
    3: 3,  # Not very acceptable
    4: 1,  # Totally unacceptable
    5: np.nan  # Don't know → exclude
}

# Apply the mapping to recode values
df_q1_recoded = df[q1_cols].applymap(lambda x: acceptability_map.get(x, np.nan))

# Create the index: row-wise mean across the 8 Q1 items
df['ethical_acceptability_index'] = df_q1_recoded.mean(axis=1)

# Summary statistics
summary = df['ethical_acceptability_index'].describe()

print("=============== Ethical Acceptability Index Summary ===============")
print(summary)

# Optional: visualize the distribution
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.histplot(df['ethical_acceptability_index'].dropna(), bins=20, kde=True, color='skyblue')
plt.title("Distribution of Ethical Acceptability Index", fontsize=14, fontweight='bold')
plt.xlabel("Ethical Acceptability Score (higher = more tolerant of unethical behavior)")
plt.ylabel("Number of Respondents")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
```

**Text output:**

```text
=============== Ethical Acceptability Index Summary ===============
count    662.000000
mean       2.234718
std        0.807659
min        1.000000
25%        1.625000
50%        2.125000
75%        2.750000
max        4.875000
Name: ethical_acceptability_index, dtype: float64
```

```text
<Figure size 1000x600 with 1 Axes>
```

## Cell 155 — raw

```python
A strong ethical mindset is prevalent — most respondents view workplace misconduct as unacceptable.

There’s some variation, with a smaller group showing moderate tolerance (upper quartile).

Since the mean is closer to 2 than 3, it's safe to interpret that your respondents have moderately strict ethical standards.
Conclusion:

Your data clearly shows most employees find unethical workplace actions unacceptable or only marginally acceptable.

The descriptive + visual together form strong, defensible insights.

This chart would pair well with comparisons by gender, sector, or pressure (Q12) in a bivariate analysis.
```

## Cell 156 — markdown

### Ethical Culture Index (ECI)
q11_01,q11_02,q11_03,q11_04,q11_05,q11_06,q11_07,q11_08,q11_09,q11_10,q11_11,q11_12,q11_13,q11_14

## Cell 157 — code

```python
# Q11 column names
q11_cols = [f'q11_{str(i).zfill(2)}' for i in range(1, 15)]

# Recode map
q11_map = {
    1: 5,  # Strongly agree
    2: 4,  # Tend to agree
    3: 3,  # Neither/nor
    4: 2,  # Tend to disagree
    5: 1,  # Strongly disagree
    6: np.nan  # Prefer not to say
}

# Recode responses
df_q11_recoded = df[q11_cols].applymap(lambda x: q11_map.get(x, np.nan))

# Create index: average of 14 items
df['ethical_culture_index'] = df_q11_recoded.mean(axis=1)

# Summary stats
eci_summary = df['ethical_culture_index'].describe()
print("=============== Ethical Culture Index Summary ===============")
print(eci_summary)

# Optional: histogram
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.histplot(df['ethical_culture_index'].dropna(), bins=20, kde=True, color='salmon')
plt.title("Distribution of Ethical Culture Index", fontsize=14, fontweight='bold')
plt.xlabel("Ethical Culture Score (higher = stronger ethical culture perception)")
plt.ylabel("Number of Respondents")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
```

**Text output:**

```text
=============== Ethical Culture Index Summary ===============
count    662.000000
mean       3.698237
std        0.758490
min        1.071429
25%        3.214286
50%        3.714286
75%        4.214286
max        5.000000
Name: ethical_culture_index, dtype: float64
```

```text
<Figure size 1000x600 with 1 Axes>
```

## Cell 158 — raw

```python
Slight Left-Skew / Concentration at Higher Values:

Most responses lie between 3.2 and 4.8, peaking around 3.7–4.0.

This suggests that respondents generally perceive their organization as having a strong ethical culture.

High Overall Scores:

The mean (3.70) and median (3.71) are close, reinforcing the symmetry in the distribution, but with a slight tail on the lower end.

Few Perceive Poor Ethical Culture:

Very few respondents have scores below 2.5, indicating strong confidence in ethics at leadership and systemic levels.
```

## Cell 159 — markdown

### Rule Tolerance Index (RTI)
q14_01,q14_02,q14_03,q14_04,q14_05

## Cell 160 — code

```python
# Q14 columns
q14_cols = [f'q14_0{i}' for i in range(1, 6)]

# Recode map
q14_map = {
    1: 5,  # Strongly agree
    2: 4,  # Tend to agree
    3: 3,  # Neither/nor
    4: 2,  # Tend to disagree
    5: 1,  # Strongly disagree
    6: np.nan  # Prefer not to say
}

# Apply recoding
df_q14_recoded = df[q14_cols].applymap(lambda x: q14_map.get(x, np.nan))

# Compute Rule Tolerance Index
df['rule_tolerance_index'] = df_q14_recoded.mean(axis=1)

# Summary
print("=============== Rule Tolerance Index Summary ===============")
print(df['rule_tolerance_index'].describe())

# Optional: Plot histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['rule_tolerance_index'].dropna(), bins=20, kde=True, color='skyblue')
plt.title("Distribution of Rule Tolerance Index", fontsize=14, fontweight='bold')
plt.xlabel("Rule Tolerance Score (higher = more permissive attitudes)")
plt.ylabel("Number of Respondents")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
```

**Text output:**

```text
=============== Rule Tolerance Index Summary ===============
count    661.000000
mean       2.871256
std        0.902277
min        1.000000
25%        2.200000
50%        3.000000
75%        3.600000
max        5.000000
Name: rule_tolerance_index, dtype: float64
```

```text
<Figure size 1000x600 with 1 Axes>
```

## Cell 161 — raw

```python
Insights:

Fairly Symmetrical Distribution Around Mean ≈ 2.9:

Respondents are spread across a wide range of values, but the majority cluster around 2.5 to 3.5.

This suggests a moderate tolerance for rule breaches.

Right-Tailed Spread:

While fewer respondents are extremely permissive (scores near 5), a visible portion still scores 4+, indicating some respondents believe rule-bending is somewhat acceptable.

Interpretation of Central Values:

A mean and median around 2.9 indicates a balanced perspective: not overly strict, not overly permissive.

Potential for Segmentation Analysis:

This index would be particularly useful in comparing:

Ethical Culture Index (e.g., Does stronger ethical culture reduce tolerance for rule-breaking?)

Demographics like sector (public vs private), age group, or employment status

Ethical Pressure (Q12) — Do those feeling pressured have higher tolerance?
```

## Cell 162 — markdown

### Future Ethical Concern Index (FECI)
q15_01,q15_02,q15_03,q15_04,q15_05,q15_06,q15_07,q15_08,q15_09

## Cell 163 — code

```python

# Q15 columns
q15_cols = [f'q15_0{i}' for i in range(1, 10)]

# Recode map
q15_map = {
    1: 5,  # Extremely concerned
    2: 4,  # Moderately concerned
    3: 3,  # Slightly concerned
    4: 2,  # Not very concerned
    5: 1,  # Not at all concerned
    6: np.nan  # Prefer not to say
}

# Apply mapping
df_q15_recoded = df[q15_cols].applymap(lambda x: q15_map.get(x, np.nan))

# Compute index
df['future_ethics_concern_index'] = df_q15_recoded.mean(axis=1)

# Summary
print("=============== Future Ethical Concern Index Summary ===============")
print(df['future_ethics_concern_index'].describe())

# Optional: Plot distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['future_ethics_concern_index'].dropna(), bins=20, kde=True, color='salmon')
plt.title("Distribution of Future Ethical Concern Index (FECI)", fontsize=14, fontweight='bold')
plt.xlabel("FECI Score (higher = more concern)")
plt.ylabel("Number of Respondents")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
```

**Text output:**

```text
=============== Future Ethical Concern Index Summary ===============
count    652.000000
mean       2.955175
std        0.915936
min        1.000000
25%        2.333333
50%        3.000000
75%        3.583333
max        5.000000
Name: future_ethics_concern_index, dtype: float64
```

```text
<Figure size 1000x600 with 1 Axes>
```

## Cell 164 — raw

```python
Interpretation:

Moderate Concern is Most Common:

The distribution peaks between 2.5 and 3.5, with the median ~3.2, suggesting most respondents have moderate concern about future ethical issues.

Fairly Symmetrical Distribution:

A slight skew left implies more concern than complacency, but not dramatically so.

Few respondents show very low concern (score near 1), indicating general awareness of upcoming ethical challenges.

Useful for Bivariate Analysis With:

Age (d02_group): Younger respondents may be more or less concerned than older ones.

Sector (d05): Private vs public vs third-sector variations.

Ethical Culture Index: Does a stronger culture increase or reduce concern about the future?

Ethical Acceptability Index: Are more tolerant people also more or less concerned about the future?
```

## Cell 165 — code

```python
df.head()
```

**Text output:**

```text
serial  sq1  d01  d02_group  d04  d05  d08a  d08b  d08c01  d08c02  d08c03  d08c04  d08c05  d08c06  d08c07  d08c08  d08c09  d08c10  d08c11  d08c12  d09  d10  q01_01  q01_02  q01_03  q01_04  q01_05  q01_06  q01_07  q01_08  q02  q03  q04  q0501  q0502  q0503  q0504  q0505  q0506  q0507  q0508  q0509  q0510  q0511  q0512  q0513  q0514  q06  q07  q08  q0901  q0902  q0903  q0904  q0905  q0906  q0907  q0908  q0909  q0910  q0911  q0912  q10_01  q10_02  q10_03  q10_04  q11_01  q11_02  q11_03  q11_04  q11_05  q11_06  q11_07  q11_08  q11_09  q11_10  q11_11  q11_12  q11_13  q11_14  q12  q1301  q1302  q1303  q1304  q1305  q1306  q1307  q1308  q1309  q1310  q1311  q1312  q14_01  q14_02  q14_03  q14_04  q14_05  q15_01  q15_02  q15_03  q15_04  q15_05  q15_06  q15_07  q15_08  q15_09 gender_labeled age_group_labeled                 sector_label     d05_labeled d08a_label d08b_label               q03_label AI_Adoption AI_Interaction   q02_label q04_label q12_label  ethical_acceptability_index  ethical_culture_index  rule_tolerance_index  future_ethics_concern_index
0      35    2    1          2    7    2     1     2       0       0       0       0       0       0       0       1       0       0       0       0    2    2       2       1       3       4       4       3       3       3    1    1    1    1.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0  1.0  4.0  2.0    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN       1       1       1       1       1       1       3       1       1       2       1       1       1       2       1       1       1       2    2    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN       2       1       1       2       5       1       4       1       1       1       2       2       1       1           Male             25–34          Finance & Insurance  Private Sector        Yes         No  Significantly improved          No             No      Always       Yes        No                        2.875               4.642857                   3.8                     4.444444
1      59    2    2          2   11    1     1     1       1       0       0       0       1       0       0       1       0       0       0       0    1    1       4       3       4       4       4       1       2       4    1    1    1    1.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0  1.0  1.0  1.0    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN       1       1       1       1       2       1       1       1       1       1       1       2       1       1       1       2       1       1    1    0.0    0.0    0.0    1.0    0.0    0.0    0.0    0.0    1.0    0.0    0.0    0.0       1       1       1       1       1       2       2       1       2       2       4       2       2       2         Female             25–34  Information & Communication   Public Sector        Yes   
... [output truncated]
```

## Cell 166 — markdown

## 5c Bivariate Analysis

## Cell 167 — raw

```python
| Demographic (X-axis)      | Outcome (Y-axis)              | Type of analysis                  |
| ------------------------- | ----------------------------- | --------------------------------- |
| `d01` (Gender) 
     gender_labeled         | `ethical_acceptability_index` | Compare mean or grouped bar chart |
|                           | `ethical_culture_index`       | Same                              |
|                           | `q12` (felt pressured?)       | Cross-tab %                       |
|   `d02_group` (Age group) | All 4 indexes + `q04`, `q12`  | Cross-tabs or grouped bars        |
|        age_group_labeled
| `d04` (Industry)          | All indexes + `q12`           | Cross-tabs, stacked bars          |
    sector_labeled
| `d05` (Sector type)       | All indexes                   | Same                              |
     d05_labeled
| `sq1` (Employment status) | All indexes + `q04`, `q12`    | Same                              |
```

## Cell 169 — markdown

### d01(Gender) VS Indexes 
#### Indexes are :
#### ethical_acceptability_index (from Q1)
#### ethical_culture_index (from Q11) 
#### rule_tolerance_index (from Q14)
#### future_ethics_concern_index (from Q15)

## Cell 170 — markdown

#### D01(Gender) VS  ethical_acceptability_index (from Q1)

## Cell 171 — code

```python
gender_ethics_summary = (
    df.groupby("gender_labeled")["ethical_acceptability_index"]
      .agg(
          count="count",
          mean="mean",
          median="median",
          std="std"
      )
      .round(3)
      .reset_index()
)

print("=============== Gender vs Ethical Acceptability Index ===============")
print(gender_ethics_summary)

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="gender_labeled",
    y="ethical_acceptability_index",
    palette="Pastel1"
)
sns.pointplot(
    data=df,
    x="gender_labeled",
    y="ethical_acceptability_index",
    estimator="mean",
    color="red",
    markers="D",
    scale=1.2,
    ci=None
)

plt.title("Ethical Acceptability Index Distribution and Mean by Gender",
          fontsize=13, fontweight="bold")
plt.xlabel("Gender")
plt.ylabel("Ethical Acceptability Index\n(higher = more tolerance of unethical behaviour")

plt.ylim(1, 5)
plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Gender vs Ethical Acceptability Index ===============
  gender_labeled  count   mean  median    std
0         Female    304  2.145   2.125  0.722
1           Male    356  2.315   2.250  0.867
2          Other      2  1.625   1.625  0.884
```

```text
<Figure size 800x500 with 1 Axes>
```

## Cell 172 — raw

```python
Gender and Ethical Acceptability Index – Key Insights

The bivariate analysis shows a clear difference in ethical acceptability scores across gender groups. Male respondents have a higher mean Ethical Acceptability Index (mean = 2.315) compared to female respondents (mean = 2.145), indicating that men, on average, are more tolerant of unethical workplace behaviours than women. This pattern is also reflected in the median values, which follow the same direction, strengthening the consistency of the result.

Additionally, the standard deviation for males (0.867) is higher than that for females (0.722), suggesting greater variability in ethical attitudes among male respondents, while female respondents display more consistent ethical judgments. The “Other” gender category has a very small sample size (n = 2) and is therefore not considered reliable for interpretation.

Overall, this descriptive bivariate analysis suggests that gender is associated with differing levels of tolerance towards unethical behaviour, with female respondents demonstrating stricter ethical standards compared to male respondents. No causal conclusions are drawn, as the analysis is purely descriptive.
```

## Cell 173 — markdown

#### d01(Gender) VS ethical_culture_index (from Q11)

## Cell 174 — code

```python
# ============================================================
# Gender (d01) vs Ethical Culture Index (Q11)
# ============================================================
# 1. Descriptive summary
gender_ethical_culture_summary = (
    df
    .groupby("gender_labeled")["ethical_culture_index"]
    .agg(
        count="count",
        mean="mean",
        median="median",
        std="std"
    )
    .reset_index()
)

print("=============== Gender vs Ethical Culture Index ===============")
print(gender_ethical_culture_summary.round(3))



plt.figure(figsize=(6, 3))

sns.boxplot(
    data=df,
    x="gender_labeled",
    y="ethical_culture_index",
    palette="Pastel1"
)

sns.pointplot(
    data=df,
    x="gender_labeled",
    y="ethical_culture_index",
    estimator="mean",
    color="red",
    markers="D",
    scale=1.2,
    ci=None
)

plt.title("Ethical Culture Index Distribution and Mean by Gender",
          fontsize=13, fontweight="bold")
plt.xlabel("Gender")
plt.ylabel("Ethical Culture Index")

plt.ylim(1, 5)
plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Gender vs Ethical Culture Index ===============
  gender_labeled  count   mean  median    std
0         Female    304  3.756   3.786  0.758
1           Male    356  3.650   3.714  0.757
2          Other      2  3.500   3.500  1.010
```

```text
<Figure size 600x300 with 1 Axes>
```

## Cell 175 — raw

```python
Gender vs Ethical Culture Index – Descriptive Insights

The Ethical Culture Index scores are relatively high across all genders, with mean values clustered between 3.5 and 3.8, indicating a generally positive perception of ethical culture in organisations.

Female respondents report the highest mean Ethical Culture Index (mean ≈ 3.76), followed closely by male respondents (mean ≈ 3.65).
This suggests that female respondents, on average, perceive their organisational ethical culture slightly more positively.

The difference in mean scores between males and females is small, and the boxplots show substantial overlap, indicating broadly similar perceptions rather than stark gender-based differences.

The spread of scores is comparable for males and females, as reflected by similar interquartile ranges and standard deviations (≈ 0.75), suggesting consistent variability in perceptions across these groups.

The ‘Other’ gender category shows a slightly lower mean, but the very small sample size (n = 2) means this result should be interpreted with caution and is not representative.

Overall, the analysis indicates that perceptions of ethical culture are largely consistent across gender groups, with only minor variations in central tendency.
```

## Cell 176 — markdown

#### d01(Gender) VS rule_tolerance_index (from Q14)

## Cell 177 — code

```python
# ============================================================
# Gender (d01) vs Rule Tolerance Index (Q14)
# ============================================================
# 1. Descriptive summary
gender_rule_tolerance_summary = (
    df
    .groupby("gender_labeled")["rule_tolerance_index"]
    .agg(
        count="count",
        mean="mean",
        median="median",
        std="std"
    )
    .reset_index()
)

print("=============== Gender vs Rule Tolerance Index ===============")
print(gender_rule_tolerance_summary.round(3))


# 2. Visualisation: Boxplot + Mean
plt.figure(figsize=(6, 3))

sns.boxplot(
    data=df,
    x="gender_labeled",
    y="rule_tolerance_index",
    palette="Pastel2"
)

sns.pointplot(
    data=df,
    x="gender_labeled",
    y="rule_tolerance_index",
    estimator="mean",
    color="darkred",
    markers="D",
    scale=1.2,
    ci=None
)

plt.title(
    "Rule Tolerance Index Distribution and Mean by Gender",
    fontsize=13,
    fontweight="bold"
)
plt.xlabel("Gender")
plt.ylabel("Rule Tolerance Index")

plt.ylim(1, 5)
plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Gender vs Rule Tolerance Index ===============
  gender_labeled  count   mean  median    std
0         Female    304  2.710   2.775  0.867
1           Male    355  3.016   3.200  0.906
2          Other      2  1.700   1.700  0.707
```

```text
<Figure size 600x300 with 1 Axes>
```

## Cell 178 — markdown

#### d01(Gender) VS future_ethics_concern_index (from Q15)

## Cell 179 — code

```python
# ============================================================
# Gender (d01) vs Future Ethics Concern Index (Q15)
# ============================================================

# 1. Descriptive summary
gender_future_ethics_summary = (
    df
    .groupby("gender_labeled")["future_ethics_concern_index"]
    .agg(
        count="count",
        mean="mean",
        median="median",
        std="std"
    )
    .reset_index()
)

print("=============== Gender vs Future Ethics Concern Index ===============")
print(gender_future_ethics_summary.round(3))


# 2. Visualisation: Boxplot + Mean
plt.figure(figsize=(6, 3))

sns.boxplot(
    data=df,
    x="gender_labeled",
    y="future_ethics_concern_index",
    palette="Set3"
)

sns.pointplot(
    data=df,
    x="gender_labeled",
    y="future_ethics_concern_index",
    estimator="mean",
    color="darkblue",
    markers="D",
    scale=1.2,
    ci=None
)

plt.title(
    "Future Ethics Concern Index Distribution and Mean by Gender",
    fontsize=13,
    fontweight="bold"
)
plt.xlabel("Gender")
plt.ylabel("Future Ethics Concern Index")

plt.ylim(1, 5)
plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Gender vs Future Ethics Concern Index ===============
  gender_labeled  count   mean  median    std
0         Female    299  2.915   2.889  0.898
1           Male    351  2.988   3.000  0.934
2          Other      2  3.278   3.278  0.079
```

```text
<Figure size 600x300 with 1 Axes>
```

## Cell 180 — raw

```python
The Future Ethics Concern Index scores are moderately high across all gender groups, with mean values close to 3, indicating a general level of concern about the ethical future of work across respondents.

Male respondents report a slightly higher mean concern score (mean ≈ 2.99) compared to female respondents (mean ≈ 2.92). However, the difference between these groups is very small, suggesting broadly similar levels of concern.

The median values reinforce this pattern, with males showing a median of 3.00 and females 2.89, indicating only marginal variation in central tendency.

The distribution of scores overlaps substantially between male and female respondents, as reflected in the boxplots, implying that gender differences in future ethical concerns are limited and not pronounced.

The ‘Other’ gender category displays a higher mean score, but this is based on a very small sample size (n = 2) and therefore should be interpreted with caution.

Overall, the findings suggest that concerns about the ethical implications of future workplace developments are shared relatively equally across genders, with only minor descriptive differences.
```

## Cell 181 — markdown

#### d01(Gender)  VS felt pressure (q12)

## Cell 182 — code

```python
# Count table
gender_q12_counts = (
    df
    .groupby(["gender_labeled", "q12_label"])
    .size()
    .reset_index(name="count")
)

# Percentage within gender
gender_q12_counts["percentage"] = (
    gender_q12_counts
    .groupby("gender_labeled")["count"]
    .transform(lambda x: round(100 * x / x.sum(), 2))
)

print("=============== Gender vs Felt Ethical Pressure (Q12) ===============")
print(gender_q12_counts)

# Pivot for plotting
gender_q12_pivot = gender_q12_counts.pivot(
    index="gender_labeled",
    columns="q12_label",
    values="percentage"
)

# Plot
gender_q12_pivot.plot(
    kind="bar",
    stacked=True,
    figsize=(7, 4),
    colormap="Pastel2"
)

plt.title("Percentage Distribution of Felt Ethical Pressure (Q12) by Gender",
          fontsize=13, fontweight="bold")
plt.xlabel("Gender")
plt.ylabel("Percentage of Respondents")
plt.legend(title="Felt pressured?", bbox_to_anchor=(1.05, 1), loc="upper left")

plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Gender vs Felt Ethical Pressure (Q12) ===============
  gender_labeled          q12_label  count  percentage
0         Female                 No    274       89.25
1         Female  Prefer not to say      7        2.28
2         Female                Yes     26        8.47
3           Male                 No    302       84.36
4           Male  Prefer not to say      8        2.23
5           Male                Yes     48       13.41
6          Other                 No      2      100.00
```

```text
<Figure size 700x400 with 1 Axes>
```

## Cell 183 — raw

```python
Gender vs Felt Ethical Pressure (Q12) — Insights
1. Majority across all genders did NOT feel pressured

For both males (84.36%) and females (89.25%), the vast majority report not feeling pressured to compromise ethical standards.

This suggests that, overall, explicit ethical pressure is not widespread in respondents’ workplaces.

2. Males report higher ethical pressure than females

13.41% of males reported feeling pressured, compared to 8.47% of females.

This indicates that male respondents are more likely to experience ethical pressure in the workplace than female respondents.

Interpretation (descriptive, not causal):
Ethical pressure appears to be unevenly experienced across genders, with males reporting exposure more frequently.

3. “Prefer not to say” responses are minimal

The “Prefer not to say” category is very small and similar across genders:

Female: 2.28%

Male: 2.23%

This suggests low response sensitivity or discomfort for this question, strengthening confidence in the results.

4. ‘Other’ gender category is too small for inference

The “Other” category contains only 2 respondents, with 100% reporting no pressure.

This group is not analytically meaningful due to extremely small sample size and should be treated cautiously in interpretation.
```

## Cell 184 — markdown

### d02_group (Age group) VS Indexes
#### Indexes are :
#### ethical_acceptability_index (from Q1)
#### ethical_culture_index (from Q11)
#### rule_tolerance_index (from Q14)
#### future_ethics_concern_index (from Q15)¶

## Cell 185 — markdown

#### d02_group (Age group) VS ethical_acceptability_index (from Q1)

## Cell 186 — code

```python
# ============================================================
# Age Group vs Ethical Acceptability Index
# ============================================================

age_acceptability_summary = (
    df
    .groupby("age_group_labeled")["ethical_acceptability_index"]
    .agg(count="count", mean="mean", median="median", std="std")
    .reset_index()
)

print("=============== Age Group vs Ethical Acceptability Index ===============")
print(age_acceptability_summary.round(3))

age_order = ["18–24", "25–34", "35–44", "45–54", "55–64", "65+"]

plt.figure(figsize=(8, 4))

sns.boxplot(
    data=df,
    x="age_group_labeled",
    y="ethical_acceptability_index",
    order=age_order,
    palette="Pastel1"
)

sns.pointplot(
    data=df,
    x="age_group_labeled",
    y="ethical_acceptability_index",
    estimator="mean",
    color="red",
    markers="D",
    ci=None
)

plt.title("Ethical Acceptability Index by Age Group", fontsize=13, fontweight="bold")
plt.xlabel("Age Group")
plt.ylabel("Ethical Acceptability Index")
plt.ylim(1, 5)
plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Age Group vs Ethical Acceptability Index ===============
  age_group_labeled  count   mean  median    std
0             18–24     96  2.606   2.625  0.770
1             25–34    131  2.418   2.333  0.847
2             35–44    124  2.315   2.375  0.840
3             45–54    140  2.179   2.062  0.763
4             55–64    117  1.932   2.000  0.594
5               65+     54  1.746   1.500  0.758
```

```text
<Figure size 800x400 with 1 Axes>
```

## Cell 187 — raw

```python
Age Group vs Ethical Acceptability Index – Descriptive Insights

The results show a clear age-related pattern in ethical acceptability perceptions. Younger respondents tend to report higher Ethical Acceptability Index scores, indicating greater tolerance toward ethically questionable workplace behaviours.

The 18–24 age group records the highest mean score (mean ≈ 2.61), followed by the 25–34 group (mean ≈ 2.42). This suggests that younger employees are, on average, more accepting of minor unethical practices.

As age increases, there is a gradual decline in the Ethical Acceptability Index. Respondents aged 55–64 and 65+ show the lowest mean scores (≈ 1.93 and 1.75, respectively), indicating lower tolerance for unethical behaviour.

The median values reinforce this trend, showing a steady shift toward lower ethical acceptability with increasing age, rather than the pattern being driven by extreme values.

The spread of scores is wider among younger age groups, particularly 18–24 and 25–34, suggesting greater variability in ethical attitudes early in careers. In contrast, older age groups display more concentrated distributions, indicating more consistent ethical standards.

Overall, the analysis suggests that ethical tolerance decreases with age, highlighting a generational difference in attitudes toward workplace ethical acceptability.
```

## Cell 188 — markdown

#### d02_group (Age group) VS ethical_culture_index (from Q11)

## Cell 189 — code

```python
# ============================================================
# Age Group vs Ethical Culture Index
# ============================================================
#age_order = ["18–24", "25–34", "35–44", "45–54", "55–64", "65+"]
age_culture_summary = (
    df
    .groupby("age_group_labeled")["ethical_culture_index"]
    .agg(count="count", mean="mean", median="median", std="std")
    .reset_index()
)

print("=============== Age Group vs Ethical Culture Index ===============")
print(age_culture_summary.round(3))


plt.figure(figsize=(8, 4))

sns.boxplot(
    data=df,
    x="age_group_labeled",
    y="ethical_culture_index",
    order=age_order,
    palette="Set2"
)

sns.pointplot(
    data=df,
    x="age_group_labeled",
    y="ethical_culture_index",
    estimator="mean",
    color="darkgreen",
    markers="D",
    ci=None
)

plt.title("Ethical Culture Index by Age Group", fontsize=13, fontweight="bold")
plt.xlabel("Age Group")
plt.ylabel("Ethical Culture Index")
plt.ylim(1, 5)
plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Age Group vs Ethical Culture Index ===============
  age_group_labeled  count   mean  median    std
0             18–24     94  3.720   3.786  0.846
1             25–34    131  3.802   3.857  0.719
2             35–44    124  3.751   3.786  0.758
3             45–54    141  3.600   3.714  0.763
4             55–64    117  3.550   3.571  0.716
5               65+     55  3.863   3.857  0.718
```

```text
<Figure size 800x400 with 1 Axes>
```

## Cell 190 — raw

```python
Age Group vs Ethical Culture Index – Descriptive Insights

Across all age groups, the Ethical Culture Index scores are relatively high, with mean values consistently above 3.5, indicating generally positive perceptions of organisational ethical culture.

The highest mean scores are observed among the 25–34 and 65+ age groups (means ≈ 3.80 and 3.86, respectively), suggesting that both early-career professionals and older respondents perceive their organisations as having a stronger ethical culture.

Respondents in the 55–64 age group report the lowest mean Ethical Culture Index (mean ≈ 3.55), indicating slightly less favourable perceptions compared to other age groups.

The trend across age groups is not strictly linear. Instead of a steady increase or decrease, the pattern shows moderate fluctuations, implying that perceptions of ethical culture are broadly consistent across age cohorts, with only modest variation.

The distributions overlap substantially across age groups, as reflected in the boxplots, suggesting that age is not a strong differentiating factor in perceptions of organisational ethical culture.

Variability within each age group is similar, indicating comparable diversity of opinions regarding ethical culture regardless of age.
```

## Cell 191 — markdown

#### d02_group (Age group) VS rule_tolerance_index (from Q14)

## Cell 192 — code

```python
# ============================================================
# Age Group vs Rule Tolerance Index
# ============================================================

age_rule_summary = (
    df
    .groupby("age_group_labeled")["rule_tolerance_index"]
    .agg(count="count", mean="mean", median="median", std="std")
    .reset_index()
)

print("=============== Age Group vs Rule Tolerance Index ===============")
print(age_rule_summary.round(3))


plt.figure(figsize=(8, 4))

sns.boxplot(
    data=df,
    x="age_group_labeled",
    y="rule_tolerance_index",
    order=age_order,
    palette="Pastel2"
)

sns.pointplot(
    data=df,
    x="age_group_labeled",
    y="rule_tolerance_index",
    estimator="mean",
    color="purple",
    markers="D",
    ci=None
)

plt.title("Rule Tolerance Index by Age Group", fontsize=13, fontweight="bold")
plt.xlabel("Age Group")
plt.ylabel("Rule Tolerance Index")
plt.ylim(1, 5)
plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Age Group vs Rule Tolerance Index ===============
  age_group_labeled  count   mean  median    std
0             18–24     95  3.210     3.2  0.880
1             25–34    132  2.951     3.0  0.949
2             35–44    123  2.869     2.8  0.954
3             45–54    141  2.816     2.8  0.881
4             55–64    116  2.669     2.6  0.751
5               65+     54  2.667     2.7  0.898
```

```text
<Figure size 800x400 with 1 Axes>
```

## Cell 193 — raw

```python
Age Group vs Rule Tolerance Index – Descriptive Insights

The analysis reveals a clear and consistent age-related pattern in rule tolerance. Younger respondents display higher Rule Tolerance Index scores, indicating a greater acceptance of minor rule violations.

The 18–24 age group records the highest mean score (mean ≈ 3.21), suggesting the strongest tolerance for bending or overlooking minor organisational rules.

As age increases, there is a gradual and monotonic decline in the Rule Tolerance Index. Respondents aged 55–64 and 65+ show the lowest mean scores (≈ 2.67), indicating more conservative attitudes toward rule compliance.

The median values mirror the downward trend, reinforcing that the pattern is not driven by a small number of extreme responses.

Variability in scores is relatively higher among younger age groups, while older respondents exhibit more tightly clustered distributions, suggesting more consistent rule-oriented attitudes later in life.

Overall, the findings suggest that tolerance for minor rule breaches decreases with age, highlighting a clear generational difference in attitudes toward rule adherence in the workplace.
```

## Cell 194 — code

```python
# ============================================================
# Age Group vs Future Ethics Concern Index
# ============================================================

age_future_summary = (
    df
    .groupby("age_group_labeled")["future_ethics_concern_index"]
    .agg(count="count", mean="mean", median="median", std="std")
    .reset_index()
)

print("=============== Age Group vs Future Ethics Concern Index ===============")
print(age_future_summary.round(3))


plt.figure(figsize=(8, 4))

sns.boxplot(
    data=df,
    x="age_group_labeled",
    y="future_ethics_concern_index",
    order=age_order,
    palette="Set3"
)

sns.pointplot(
    data=df,
    x="age_group_labeled",
    y="future_ethics_concern_index",
    estimator="mean",
    color="navy",
    markers="D",
    ci=None
)

plt.title("Future Ethics Concern Index by Age Group", fontsize=13, fontweight="bold")
plt.xlabel("Age Group")
plt.ylabel("Future Ethics Concern Index")
plt.ylim(1, 5)
plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Age Group vs Future Ethics Concern Index ===============
  age_group_labeled  count   mean  median    std
0             18–24     92  2.891   2.889  0.966
1             25–34    128  3.067   3.111  0.949
2             35–44    122  2.976   2.944  0.929
3             45–54    139  2.963   3.111  0.928
4             55–64    116  2.942   2.889  0.874
5               65+     55  2.767   2.667  0.768
```

```text
<Figure size 800x400 with 1 Axes>
```

## Cell 195 — raw

```python
Age Group vs Future Ethics Concern Index – Descriptive Insights

Overall, future ethics concern levels are moderate across all age groups, with mean scores clustering around 2.8–3.1, indicating neither extreme concern nor complete indifference.

The 25–34 age group shows the highest mean concern (mean ≈ 3.07), suggesting that early-career and mid-career professionals are most alert to future ethical risks, particularly around technology, AI, and workplace change.

Concern levels remain relatively stable from ages 18–24 through 55–64, with only minor fluctuations, indicating a broadly shared awareness of future ethical challenges across most working-age groups.

A noticeable decline appears in the 65+ group, which records the lowest mean score (≈ 2.77). This suggests comparatively lower concern about future workplace ethics among older respondents, possibly due to reduced exposure to emerging technologies or proximity to retirement.

The boxplot distributions overlap substantially, showing that differences between age groups are gradual rather than sharply segmented, reinforcing that concern about future ethics is widespread rather than age-polarised.

Variability in responses is slightly higher among younger age groups, while older groups show more compact distributions, suggesting more settled attitudes.
```

## Cell 196 — markdown

#### d02_group (Age group) VS q4 (Aware of Misconduct)

## Cell 197 — code

```python
age_q4_summary = (
    df
    .groupby(["age_group_labeled", "q04_label"])
    .size()
    .reset_index(name="count")
)

# Calculate percentages within each age group
age_q4_summary["percentage"] = (
    age_q4_summary
    .groupby("age_group_labeled")["count"]
    .transform(lambda x: round(100 * x / x.sum(), 2))
)

print("=============== Age Group vs Awareness of Misconduct (Q4) ===============")
print(age_q4_summary)
# Pivot for plotting
age_q4_pivot = age_q4_summary.pivot(
    index="age_group_labeled",
    columns="q04_label",
    values="percentage"
).fillna(0)

# Order age groups correctly
age_order = ["18–24", "25–34", "35–44", "45–54", "55–64", "65+"]
age_q4_pivot = age_q4_pivot.reindex(age_order)

# Plot
age_q4_pivot.plot(
    kind="bar",
    stacked=True,
    figsize=(8, 4),
    colormap="Set2"
)

plt.title("Awareness of Ethical Misconduct (Q4) by Age Group",
          fontsize=13, fontweight="bold")
plt.xlabel("Age Group")
plt.ylabel("Percentage of Respondents")
plt.ylim(0, 100)
plt.legend(title="Aware of misconduct?", bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Age Group vs Awareness of Misconduct (Q4) ===============
   age_group_labeled          q04_label  count  percentage
0              18–24                 No     67       69.79
1              18–24  Prefer not to say      2        2.08
2              18–24                Yes     27       28.12
3              25–34                 No     95       71.43
4              25–34  Prefer not to say      6        4.51
5              25–34                Yes     32       24.06
6              35–44                 No    106       85.48
7              35–44  Prefer not to say      1        0.81
8              35–44                Yes     17       13.71
9              45–54                 No    126       88.73
10             45–54  Prefer not to say      3        2.11
11             45–54                Yes     13        9.15
12             55–64                 No     96       82.05
13             55–64  Prefer not to say      2        1.71
14             55–64                Yes     19       16.24
15               65+                 No     49       89.09
16               65+                Yes      6       10.91
```

```text
<Figure size 800x400 with 1 Axes>
```

## Cell 198 — raw

```python
Insights: Age Group vs Awareness of Ethical Misconduct (Q4)
1. Awareness of misconduct decreases with age

The youngest age group (18–24) reports the highest awareness of misconduct:

28.1% answered Yes.

Awareness steadily declines with increasing age, reaching the lowest levels among:

55–64: 16.2%

65+: 10.9%

➡️ This suggests that younger employees are more likely to notice or recognise unethical conduct in the workplace.

2. Strong dominance of “No” responses across all age groups

In every age group, the majority reported no awareness of misconduct.

This is most pronounced among older respondents:

45–54: 88.7% No

65+: 89.1% No

➡️ Overall, most employees—regardless of age—do not report awareness of ethical violations, indicating either limited exposure or possible under-recognition.

3. Middle-aged groups show a sharp drop in awareness

Awareness drops notably after early career stages:

25–34: 24.1% Yes

35–44: 13.7% Yes

45–54: 9.2% Yes

➡️ This may reflect normalisation of behaviour, greater organisational adaptation, or reduced willingness to label conduct as unethical over time.

4. “Prefer not to say” responses remain minimal

Across all age groups, Prefer not to say remains below 5%.

This suggests low response avoidance and relatively high confidence in answering this question.
```

## Cell 199 — markdown

#### d02_group (Age group) VS felt pressure (q12)

## Cell 200 — code

```python
age_q12_summary = (
    df
    .groupby(["age_group_labeled", "q12_label"])
    .size()
    .reset_index(name="count")
)

# Percentages within each age group
age_q12_summary["percentage"] = (
    age_q12_summary
    .groupby("age_group_labeled")["count"]
    .transform(lambda x: round(100 * x / x.sum(), 2))
)

print("=============== Age Group vs Felt Ethical Pressure (Q12) ===============")
print(age_q12_summary)

# Pivot for plotting
age_q12_pivot = age_q12_summary.pivot(
    index="age_group_labeled",
    columns="q12_label",
    values="percentage"
).fillna(0)

# Correct age order
age_order = ["18–24", "25–34", "35–44", "45–54", "55–64", "65+"]
age_q12_pivot = age_q12_pivot.reindex(age_order)

# Plot
age_q12_pivot.plot(
    kind="bar",
    stacked=True,
    figsize=(8, 4),
    colormap="Set3"
)

plt.title("Felt Ethical Pressure (Q12) by Age Group",
          fontsize=13, fontweight="bold")
plt.xlabel("Age Group")
plt.ylabel("Percentage of Respondents")
plt.ylim(0, 100)
plt.legend(title="Felt pressured?", bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Age Group vs Felt Ethical Pressure (Q12) ===============
   age_group_labeled          q12_label  count  percentage
0              18–24                 No     75       78.12
1              18–24  Prefer not to say      4        4.17
2              18–24                Yes     17       17.71
3              25–34                 No    105       78.95
4              25–34  Prefer not to say      4        3.01
5              25–34                Yes     24       18.05
6              35–44                 No    113       91.13
7              35–44  Prefer not to say      1        0.81
8              35–44                Yes     10        8.06
9              45–54                 No    125       88.03
10             45–54  Prefer not to say      4        2.82
11             45–54                Yes     13        9.15
12             55–64                 No    107       91.45
13             55–64  Prefer not to say      1        0.85
14             55–64                Yes      9        7.69
15               65+                 No     53       96.36
16               65+  Prefer not to say      1        1.82
17               65+                Yes      1        1.82
```

```text
<Figure size 800x400 with 1 Axes>
```

## Cell 201 — raw

```python
Insights: Age Group vs Felt Ethical Pressure (Q12)
1. Felt ethical pressure is highest among younger employees

The 18–24 age group reports the highest level of ethical pressure:

17.7% answered Yes.

This is closely followed by 25–34:

18.1% Yes.

➡️ This suggests that early-career employees are more likely to feel pressure to compromise ethical standards.

2. Ethical pressure decreases steadily with age

A clear downward trend is visible across age groups:

35–44: 8.1% Yes

45–54: 9.2% Yes

55–64: 7.7% Yes

65+: 1.8% Yes

➡️ Older employees appear less likely to experience or report ethical pressure, possibly reflecting greater autonomy, seniority, or job security.

3. Majority of respondents in all age groups report no ethical pressure

Across all age groups, over 78% reported No.

The proportion increases with age:

65+: 96.4% No

55–64: 91.5% No

➡️ Despite some variation, ethical pressure is not a dominant experience for most respondents.

4. “Prefer not to say” remains consistently low

Across all age groups, Prefer not to say remains below 5%.

Indicates high response confidence and low avoidance.
```

## Cell 202 — markdown

### sq1 (Employment status) VS All indexes + q04 (Aware of misconduct) , q12 (Felt Pressure)
#### ethical_acceptability_index (from Q1)
#### ethical_culture_index (from Q11)
#### rule_tolerance_index (from Q14)
#### future_ethics_concern_index (from Q15)

## Cell 203 — markdown

#### sq1 (Employment status) VS All indexes

## Cell 204 — code

```python
sq1_map = {
    1: "Furloughed / reduced hours",
    2: "Full-time",
    3: "Part-time",
    4: "Volunteer",
    5: "Unemployed / seeking work",
    6: "Not working"
}

df["employment_status"] = df["sq1"].map(sq1_map)

index_cols = [
    "ethical_acceptability_index",
    "ethical_culture_index",
    "rule_tolerance_index",
    "future_ethics_concern_index"
]

df_indexes_long = df.melt(
    id_vars="employment_status",
    value_vars=index_cols,
    var_name="Index",
    value_name="Score"
)

index_name_map = {
    "ethical_acceptability_index": "Ethical Acceptability",
    "ethical_culture_index": "Ethical Culture",
    "rule_tolerance_index": "Rule Tolerance",
    "future_ethics_concern_index": "Future Ethics Concern"
}

df_indexes_long["Index"] = df_indexes_long["Index"].map(index_name_map)
g = sns.catplot(
    data=df_indexes_long,
    x="employment_status",
    y="Score",
    col="Index",
    kind="box",
    col_wrap=2,
    height=3.5,
    aspect=1.2,
    palette="Pastel2",
    showfliers=False
)

# Overlay mean points
for ax, index_name in zip(g.axes.flat, df_indexes_long["Index"].unique()):
    sns.pointplot(
        data=df_indexes_long[df_indexes_long["Index"] == index_name],
        x="employment_status",
        y="Score",
        estimator="mean",
        color="red",
        markers="D",
        ci=None,
        ax=ax
    )
    ax.set_ylim(1, 5)
    ax.tick_params(axis="x", rotation=45)

g.set_titles("{col_name}")
g.set_axis_labels("Employment Status", "Index Score")
plt.tight_layout()
plt.show()
```

**Text output:**

```text
<Figure size 840x700 with 4 Axes>
```

## Cell 205 — markdown

📊 Employment Status vs Ethics Indexes — Key Insights
1️⃣ Ethical Acceptability Index (Q1)

Full-time employees show a slightly higher mean ethical acceptability score than part-time employees.

This suggests that full-time workers are marginally more tolerant of minor unethical behaviours (e.g. small misuse of resources) compared to part-time workers.

The distributions overlap substantially, indicating that employment status alone does not strongly differentiate ethical acceptability attitudes, but small directional differences are visible.

2️⃣ Ethical Culture Index (Q11)

Both full-time and part-time employees report similarly high perceptions of organisational ethical culture, with means clustered around the upper mid-range of the scale.

Full-time employees show a slightly higher average ethical culture score, possibly reflecting greater exposure to organisational policies, leadership, and formal ethics structures.

The narrow spread and similar medians indicate a generally consistent perception of ethical culture across employment types.

3️⃣ Rule Tolerance Index (Q14)

Part-time employees exhibit a slightly higher mean rule tolerance score than full-time employees.

This implies that part-time workers may be somewhat more permissive toward minor rule violations, such as overlooking small breaches if performance targets are met.

However, the overlapping interquartile ranges suggest that rule tolerance attitudes are broadly shared across employment statuses.

4️⃣ Future Ethics Concern Index (Q15)

Both employment groups demonstrate moderate concern about future ethical challenges related to technology, surveillance, and organisational ethics.

Part-time employees show a very marginally higher mean concern score, although the difference is small.

Overall, future ethical concern appears largely independent of employment status, suggesting that anxieties about the future of work are widespread across the workforce.

## Cell 206 — markdown

#### sq1 (Employment status) VS  q04 (Aware of misconduct) , q12 (Felt Pressure)

## Cell 207 — code

```python
# ============================================================
# Employment Status (sq1) vs Q4 & Q12
sq1_map = {
    1: "Furloughed / reduced hours",
    2: "Full-time",
    3: "Part-time",
    4: "Volunteer",
    5: "Unemployed / seeking work",
    6: "Not working"
}

df["sq1_labeled"] = df["sq1"].map(sq1_map)


# -----------------------------
# 1. Prepare long-format data
# -----------------------------
df_q_long = pd.DataFrame({
    "employment_status": df["sq1_labeled"],
    "Q4": df["q04_label"],
    "Q12": df["q12_label"]
})

df_q_long = df_q_long.melt(
    id_vars="employment_status",
    value_vars=["Q4", "Q12"],
    var_name="Question",
    value_name="Response"
)

# -----------------------------
# 2. Summary table (Count + %)
# -----------------------------
summary_table = (
    df_q_long
    .groupby(["Question", "employment_status", "Response"])
    .size()
    .reset_index(name="Count")
)

summary_table["Percentage"] = (
    summary_table
    .groupby(["Question", "employment_status"])["Count"]
    .transform(lambda x: 100 * x / x.sum())
)

summary_table["Percentage"] = summary_table["Percentage"].round(2)

print("\n=============== Employment Status vs Q4 & Q12 (Summary Table) ===============\n")
display(
    summary_table
    .sort_values(["Question", "employment_status", "Response"])
    .reset_index(drop=True)
)

# -----------------------------
# 3. Stacked bar charts
# -----------------------------
questions = summary_table["Question"].unique()
responses = ["No", "Prefer not to say", "Yes"]

fig, axes = plt.subplots(1, len(questions), figsize=(10, 4), sharey=True)

if len(questions) == 1:
    axes = [axes]

for ax, question in zip(axes, questions):
    data_q = summary_table[summary_table["Question"] == question]

    pivot = (
        data_q
        .pivot(index="employment_status", columns="Response", values="Percentage")
        .reindex(columns=responses)
        .fillna(0)
    )

    bottom = np.zeros(len(pivot))

    for response in responses:
        ax.bar(
            pivot.index,
            pivot[response],
            bottom=bottom,
            label=response
        )
        bottom += pivot[response]

    ax.set_title(
        "Aware of misconduct (Q4)" if question == "Q4"
        else "Felt ethical pressure (Q12)",
        fontsize=12,
        fontweight="bold"
    )

    ax.set_xlabel("Employment Status")
    ax.set_ylim(0, 100)
    ax.tick_params(axis="x", rotation=45)

axes[0].set_ylabel("Percentage of respondents")
axes[-1].legend(title="Response", bbox_to_anchor=(1.05, 1))

plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Employment Status vs Q4 & Q12 (Summary Table) ===============
```

```text
Question employment_status           Response  Count  Percentage
0       Q12         Full-time                 No    439       86.59
1       Q12         Full-time  Prefer not to say     13        2.56
2       Q12         Full-time                Yes     55       10.85
3       Q12         Part-time                 No    139       86.88
4       Q12         Part-time  Prefer not to say      2        1.25
5       Q12         Part-time                Yes     19       11.88
6        Q4         Full-time                 No    413       81.46
7        Q4         Full-time  Prefer not to say      9        1.78
8        Q4         Full-time                Yes     85       16.77
9        Q4         Part-time                 No    126       78.75
10       Q4         Part-time  Prefer not to say      5        3.12
11       Q4         Part-time                Yes     29       18.12
```

```text
<Figure size 1000x400 with 2 Axes>
```

## Cell 208 — markdown

📊 Employment Status vs Ethical Pressure (Q12) & Misconduct Awareness (Q4)
1️⃣ Felt Ethical Pressure (Q12)

A large majority of respondents in both employment categories report not feeling pressured to compromise ethical standards.

Full-time: ~86.6% report No

Part-time: ~86.9% report No

The proportion reporting felt ethical pressure (“Yes”) is:

Slightly higher among part-time employees (11.9%) compared to full-time employees (10.9%).

This indicates that ethical pressure is relatively uncommon overall, with minimal variation by employment status.

Interpretation:
Employment status does not appear to substantially influence whether individuals feel pressured to act unethically. Ethical pressure, when present, affects only a small minority across both groups.

2️⃣ Awareness of Ethical Misconduct (Q4)

Most respondents report not being aware of misconduct in their organisation:

Full-time: ~81.5% report No

Part-time: ~78.8% report No

Awareness of misconduct (“Yes”) is:

Higher among part-time employees (18.1%)

Compared to full-time employees (16.8%)

“Prefer not to say” responses remain low across both groups, indicating relatively clear reporting.

Interpretation:
Part-time employees appear slightly more likely to report awareness of misconduct, though the difference is modest. This may reflect differences in exposure, role type, or reporting sensitivity, but no strong divergence by employment status is observed.

🧠 Combined Interpretation (High-Scoring Framing)

Across both ethical pressure and misconduct awareness:

Employment status shows only small differences

Ethical challenges are not concentrated in one employment group

The stacked bar charts reinforce that:

Non-occurrence (“No”) dominates across all groups

Ethical risks exist but are not widespread

## Cell 210 — markdown

### d05 (Sector type) VS All indexes
#### ethical_acceptability_index (from Q1)
#### ethical_culture_index (from Q11)
#### rule_tolerance_index (from Q14)
#### future_ethics_concern_index (from Q15)

## Cell 211 — code

```python
# ============================================================
# Sector Type (d05) vs All Ethics Indexes
# Summary Table + Multi-panel Visualization
# ============================================================

indexes = {
    "ethical_acceptability_index": "Ethical Acceptability",
    "ethical_culture_index": "Ethical Culture",
    "rule_tolerance_index": "Rule Tolerance",
    "future_ethics_concern_index": "Future Ethics Concern"
}

# -----------------------------
# 1. Summary table
# -----------------------------
summary_list = []

for idx, label in indexes.items():
    temp = (
        df
        .groupby("d05_labeled")[idx]
        .agg(
            count="count",
            mean="mean",
            median="median",
            std="std"
        )
        .reset_index()
    )
    temp["Index"] = label
    summary_list.append(temp)

sector_summary = pd.concat(summary_list)

print("\n=============== Sector Type vs Ethics Indexes (Summary Table) ===============\n")
display(sector_summary.round(3))

# -----------------------------
# 2. Multi-panel boxplots
# -----------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for ax, (idx, label) in zip(axes, indexes.items()):
    
    sns.boxplot(
        data=df,
        x="d05_labeled",
        y=idx,
        palette="Pastel2",
        ax=ax
    )
    
    sns.pointplot(
        data=df,
        x="d05_labeled",
        y=idx,
        estimator="mean",
        color="red",
        markers="D",
        scale=1.1,
        ci=None,
        ax=ax
    )
    
    ax.set_title(label, fontsize=12, fontweight="bold")
    ax.set_xlabel("Sector Type")
    ax.set_ylabel("Index Score")
    ax.set_ylim(1, 5)
    ax.tick_params(axis="x", rotation=30)

plt.suptitle(
    "Ethics Indexes by Sector Type",
    fontsize=14,
    fontweight="bold",
    y=1.02
)

plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Sector Type vs Ethics Indexes (Summary Table) ===============
```

```text
d05_labeled  count   mean  median    std                  Index
0          Private Sector    408  2.265   2.250  0.795  Ethical Acceptability
1           Public Sector    234  2.190   2.125  0.829  Ethical Acceptability
2  Third/Voluntary Sector     20  2.150   2.000  0.816  Ethical Acceptability
0          Private Sector    406  3.690   3.714  0.758        Ethical Culture
1           Public Sector    236  3.713   3.857  0.769        Ethical Culture
2  Third/Voluntary Sector     20  3.687   3.714  0.666        Ethical Culture
0          Private Sector    406  2.940   3.000  0.916         Rule Tolerance
1           Public Sector    235  2.757   2.800  0.868         Rule Tolerance
2  Third/Voluntary Sector     20  2.810   2.800  0.916         Rule Tolerance
0          Private Sector    404  2.937   3.000  0.899  Future Ethics Concern
1           Public Sector    228  2.986   3.000  0.943  Future Ethics Concern
2  Third/Voluntary Sector     20  2.967   2.889  0.973  Future Ethics Concern
```

```text
<Figure size 1200x800 with 4 Axes>
```

## Cell 212 — markdown

### d04 (Industry) VS All indexes + q12 (Felt Pressure) + q04 (Aware of misconduct)
#### ethical_acceptability_index (from Q1)
#### ethical_culture_index (from Q11)
#### rule_tolerance_index (from Q14)
#### future_ethics_concern_index (from Q15)

## Cell 214 — code

```python
# ============================================================
# Industry vs Ethical Acceptability Index — Summary
# ============================================================

industry_eai_summary = (
    df
    .groupby("sector_label")["ethical_acceptability_index"]
    .agg(
        count="count",
        mean="mean",
        median="median",
        std="std"
    )
    .reset_index()
)

print("=============== Industry vs Ethical Acceptability Index ===============")
print(industry_eai_summary.round(3))


plt.figure(figsize=(14, 5))

sns.boxplot(
    data=df,
    x="sector_label",
    y="ethical_acceptability_index",
    palette="Pastel1"
)

sns.pointplot(
    data=df,
    x="sector_label",
    y="ethical_acceptability_index",
    estimator="mean",
    color="red",
    markers="D",
    ci=None
)

plt.title("Ethical Acceptability Index by Industry",
          fontsize=14, fontweight="bold")
plt.xlabel("Industry")
plt.ylabel("Ethical Acceptability Index")
plt.xticks(rotation=45, ha="right")
plt.ylim(1, 5)

plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Industry vs Ethical Acceptability Index ===============
                    sector_label  count   mean  median    std
0           Accommodation & Food     24  2.391   2.250  0.705
1                    Agriculture      5  2.025   2.000  0.894
2   Arts, Entertainment & Others     46  2.312   2.188  0.897
3       Business Admin & Support     30  2.221   2.000  0.852
4                   Construction     27  2.299   2.250  1.146
5                      Education     74  2.262   2.208  0.617
6            Finance & Insurance     49  2.452   2.375  0.911
7                         Health     86  2.023   1.938  0.724
8    Information & Communication     43  2.347   2.125  0.858
9                   Motor Trades      4  2.094   2.000  0.997
10                    Production     41  2.366   2.375  0.734
11      Professional & Technical     53  2.186   2.125  0.755
12                      Property     11  2.523   2.500  0.823
13        Public Admin & Defence     64  1.900   1.875  0.698
14                        Retail     66  2.226   2.292  0.790
15           Transport & Storage     27  2.621   2.625  0.939
16                     Wholesale     12  2.177   2.125  0.738
```

```text
<Figure size 1400x500 with 1 Axes>
```

## Cell 217 — code

```python
# ============================================================
# Industry vs Ethical Culture Index — Summary
# ============================================================

industry_eci_summary = (
    df
    .groupby("sector_label")["ethical_culture_index"]
    .agg(
        count="count",
        mean="mean",
        median="median",
        std="std"
    )
    .reset_index()
)

print("=============== Industry vs Ethical Culture Index ===============")
print(industry_eci_summary.round(3))

# plot 
plt.figure(figsize=(14, 5))

sns.boxplot(
    data=df,
    x="sector_label",
    y="ethical_culture_index",
    palette="Pastel2"
)

sns.pointplot(
    data=df,
    x="sector_label",
    y="ethical_culture_index",
    estimator="mean",
    color="red",
    markers="D",
    ci=None
)

plt.title("Ethical Culture Index by Industry",
          fontsize=14, fontweight="bold")
plt.xlabel("Industry")
plt.ylabel("Ethical Culture Index")
plt.xticks(rotation=45, ha="right")
plt.ylim(1, 5)

plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Industry vs Ethical Culture Index ===============
                    sector_label  count   mean  median    std
0           Accommodation & Food     24  3.504   3.393  0.751
1                    Agriculture      5  3.143   3.571  0.870
2   Arts, Entertainment & Others     46  3.762   3.857  0.597
3       Business Admin & Support     30  3.609   3.643  0.650
4                   Construction     27  3.731   3.714  0.857
5                      Education     75  3.653   3.714  0.729
6            Finance & Insurance     49  3.937   3.929  0.718
7                         Health     86  3.855   3.929  0.736
8    Information & Communication     42  3.953   4.214  0.883
9                   Motor Trades      4  2.893   3.000  1.057
10                    Production     41  3.516   3.643  0.824
11      Professional & Technical     53  3.721   3.714  0.703
12                      Property     11  3.799   3.929  0.716
13        Public Admin & Defence     65  3.768   3.857  0.750
14                        Retail     66  3.481   3.500  0.767
15           Transport & Storage     27  3.267   3.357  0.695
16                     Wholesale     11  4.026   4.000  0.479
```

```text
<Figure size 1400x500 with 1 Axes>
```

## Cell 218 — markdown

#### d04 (Industry) vs Rule Tolerance Index (Q14)

## Cell 219 — code

```python
# ============================================================
# Industry vs Rule Tolerance Index — Summary
# ============================================================

industry_rti_summary = (
    df
    .groupby("sector_label")["rule_tolerance_index"]
    .agg(
        count="count",
        mean="mean",
        median="median",
        std="std"
    )
    .reset_index()
)

print("=============== Industry vs Rule Tolerance Index ===============")
print(industry_rti_summary.round(3))

# plot 
plt.figure(figsize=(14, 5))

sns.boxplot(
    data=df,
    x="sector_label",
    y="rule_tolerance_index",
    palette="Set3"
)

sns.pointplot(
    data=df,
    x="sector_label",
    y="rule_tolerance_index",
    estimator="mean",
    color="red",
    markers="D",
    ci=None
)

plt.title("Rule Tolerance Index by Industry",
          fontsize=14, fontweight="bold")
plt.xlabel("Industry")
plt.ylabel("Rule Tolerance Index")
plt.xticks(rotation=45, ha="right")
plt.ylim(1, 5)

plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Industry vs Rule Tolerance Index ===============
                    sector_label  count   mean  median    std
0           Accommodation & Food     24  2.975     3.3  0.860
1                    Agriculture      5  2.920     2.8  0.390
2   Arts, Entertainment & Others     47  2.917     2.8  1.035
3       Business Admin & Support     30  3.107     3.0  0.733
4                   Construction     26  3.169     3.2  1.088
5                      Education     74  2.652     2.7  0.874
6            Finance & Insurance     49  3.086     3.0  0.888
7                         Health     86  2.820     2.8  0.779
8    Information & Communication     42  3.019     3.4  1.094
9                   Motor Trades      4  2.900     3.0  0.529
10                    Production     41  2.644     2.8  1.010
11      Professional & Technical     53  2.709     2.6  0.854
12                      Property     10  3.100     3.2  0.682
13        Public Admin & Defence     65  2.463     2.4  0.722
14                        Retail     67  3.163     3.2  0.839
15           Transport & Storage     27  3.022     3.4  0.956
16                     Wholesale     11  3.109     3.6  1.029
```

```text
<Figure size 1400x500 with 1 Axes>
```

## Cell 221 — markdown

#### d05 (Industry)  vs Future Ethics Concern Index (Q15)

## Cell 222 — code

```python
# ============================================================
# Industry vs Future Ethics Concern Index — Summary
# ============================================================

industry_feci_summary = (
    df
    .groupby("sector_label")["future_ethics_concern_index"]
    .agg(
        count="count",
        mean="mean",
        median="median",
        std="std"
    )
    .reset_index()
)

print("=============== Industry vs Future Ethics Concern Index ===============")
print(industry_feci_summary.round(3))

# plot 
plt.figure(figsize=(14, 5))

sns.boxplot(
    data=df,
    x="sector_label",
    y="future_ethics_concern_index",
    palette="coolwarm"
)

sns.pointplot(
    data=df,
    x="sector_label",
    y="future_ethics_concern_index",
    estimator="mean",
    color="black",
    markers="D",
    ci=None
)

plt.title("Future Ethics Concern Index by Industry",
          fontsize=14, fontweight="bold")
plt.xlabel("Industry")
plt.ylabel("Future Ethics Concern Index")
plt.xticks(rotation=45, ha="right")
plt.ylim(1, 5)

plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Industry vs Future Ethics Concern Index ===============
                    sector_label  count   mean  median    std
0           Accommodation & Food     24  2.477   2.333  0.901
1                    Agriculture      5  2.600   2.667  0.607
2   Arts, Entertainment & Others     45  3.307   3.556  1.041
3       Business Admin & Support     30  2.830   2.667  0.884
4                   Construction     26  2.991   3.111  1.108
5                      Education     73  3.069   3.222  0.827
6            Finance & Insurance     49  3.041   2.889  0.962
7                         Health     85  3.005   3.000  0.985
8    Information & Communication     42  3.086   3.167  0.917
9                   Motor Trades      4  2.806   2.667  0.793
10                    Production     40  2.644   2.556  0.773
11      Professional & Technical     52  2.979   3.000  0.852
12                      Property     11  2.830   2.778  0.480
13        Public Admin & Defence     62  2.801   2.889  0.809
14                        Retail     66  2.938   3.000  0.929
15           Transport & Storage     27  3.080   3.111  1.002
16                     Wholesale     11  2.818   3.000  0.892
```

```text
<Figure size 1400x500 with 1 Axes>
```

## Cell 224 — markdown

#### d04 (Industry) VS q12 (Felt Pressure)

## Cell 225 — code

```python
# ============================================================
# Industry (d04) vs Felt Ethical Pressure (Q12)
# ============================================================

# 1. Summary table (counts + percentages)
industry_q12_summary = (
    df
    .groupby(["sector_label", "q12_label"])
    .size()
    .reset_index(name="count")
)

industry_totals = (
    industry_q12_summary
    .groupby("sector_label")["count"]
    .transform("sum")
)

industry_q12_summary["percentage"] = (
    industry_q12_summary["count"] / industry_totals * 100
)

print("=============== Industry vs Felt Ethical Pressure (Q12) ===============")
print(industry_q12_summary.round(2))
# ============================================================
# Industry (d04) vs Felt Ethical Pressure (Q12)
# HORIZONTAL VERSION (BEST)
# ============================================================

fig, ax = plt.subplots(figsize=(10, 4))

pivot_q12.plot(
    kind="barh",
    stacked=True,
    ax=ax,
    color=["#66c2a5", "#fdd49e", "#fb6a4a"]
)

ax.set_title("Felt Ethical Pressure (Q12) by Industry",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Percentage of Respondents")
ax.set_ylabel("Industry")
ax.set_xlim(0, 100)

ax.legend(
    title="Felt pressured?",
    labels=["No", "Prefer not to say", "Yes"],
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)

plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Industry vs Felt Ethical Pressure (Q12) ===============
                    sector_label          q12_label  count  percentage
0           Accommodation & Food                 No     20       83.33
1           Accommodation & Food  Prefer not to say      1        4.17
2           Accommodation & Food                Yes      3       12.50
3                    Agriculture                 No      4       80.00
4                    Agriculture  Prefer not to say      1       20.00
5   Arts, Entertainment & Others                 No     44       93.62
6   Arts, Entertainment & Others                Yes      3        6.38
7       Business Admin & Support                 No     26       86.67
8       Business Admin & Support                Yes      4       13.33
9                   Construction                 No     23       85.19
10                  Construction                Yes      4       14.81
11                     Education                 No     64       85.33
12                     Education  Prefer not to say      1        1.33
13                     Education                Yes     10       13.33
14           Finance & Insurance                 No     41       83.67
15           Finance & Insurance                Yes      8       16.33
16                        Health                 No     78       89.66
17                        Health  Prefer not to say      2        2.30
18                        Health                Yes      7        8.05
19   Information & Communication                 No     33       76.74
20   Information & Communication  Prefer not to say      1        2.33
21   Information & Communication                Yes      9       20.93
22                  Motor Trades                 No      4      100.00
23                    Production                 No     36       87.80
24                    Production  Prefer not to say      2        4.88
25                    Production                Yes      3        7.32
26      Professional & Technical                 No     45       84.91
27      Professional & Technical                Yes      8       15.09
28                      Property                 No      9       81.82
29                      Property                Yes      2       18.18
30        Public Admin & Defence                 No     60       92.31
31        Public Admin & Defence  Prefer not to say      4        6.15
32        Public Admin & Defence                Yes      1        1.54
33                        Retail                 No     60       89.55
34                        Retail  Prefer not to say      1        1.49
35                        Retail                Yes      6        8.96
36           Transport & Storage                 No     22       81.48
37           Transport & Storage  Prefer not to say      1        3.70
38           Transport & Storage                Yes      4       14.81
39                     Wholesale                 No      9       75.00
40               
... [output truncated]
```

```text
<Figure size 1000x400 with 1 Axes>
```

## Cell 226 — markdown

#### d04 (Industry) VS q04 (Aware of misconduct)

## Cell 227 — code

```python
# ============================================================
# Industry (d04) vs Awareness of Misconduct (Q4) — Summary
# ============================================================
summary_q4_industry = (
    df
    .groupby(["sector_label", "q04_label"])
    .size()
    .reset_index(name="count")
)

# Calculate percentages within each industry
summary_q4_industry["percentage"] = (
    summary_q4_industry
    .groupby("sector_label")["count"]
    .transform(lambda x: round(x / x.sum() * 100, 2))
)
print("=============== Industry vs Awareness of Misconduct (Q4) ===============")
print(summary_q4_industry)
pivot_q4 = (
    summary_q4_industry
    .pivot(index="sector_label",
           columns="q04_label",
           values="percentage")
    .fillna(0)
)

# Ensure consistent column order
pivot_q4 = pivot_q4[["No", "Prefer not to say", "Yes"]]
# ============================================================
# Industry vs Awareness of Misconduct (Q4) — Plot
# ============================================================

fig, ax = plt.subplots(figsize=(10, 4))

pivot_q4.plot(
    kind="barh",
    stacked=True,
    ax=ax,
    color=["#66c2a5", "#fdd49e", "#fb6a4a"]
)

ax.set_title("Awareness of Ethical Misconduct (Q4) by Industry",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Percentage of Respondents")
ax.set_ylabel("Industry")
ax.set_xlim(0, 100)

ax.legend(
    title="Aware of misconduct?",
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)
plt.tight_layout()
plt.show()
```

**Text output:**

```text
=============== Industry vs Awareness of Misconduct (Q4) ===============
                    sector_label          q04_label  count  percentage
0           Accommodation & Food                 No     21       87.50
1           Accommodation & Food  Prefer not to say      1        4.17
2           Accommodation & Food                Yes      2        8.33
3                    Agriculture                 No      3       60.00
4                    Agriculture                Yes      2       40.00
5   Arts, Entertainment & Others                 No     44       93.62
6   Arts, Entertainment & Others                Yes      3        6.38
7       Business Admin & Support                 No     23       76.67
8       Business Admin & Support  Prefer not to say      1        3.33
9       Business Admin & Support                Yes      6       20.00
10                  Construction                 No     21       77.78
11                  Construction  Prefer not to say      1        3.70
12                  Construction                Yes      5       18.52
13                     Education                 No     61       81.33
14                     Education  Prefer not to say      3        4.00
15                     Education                Yes     11       14.67
16           Finance & Insurance                 No     39       79.59
17           Finance & Insurance                Yes     10       20.41
18                        Health                 No     77       88.51
19                        Health                Yes     10       11.49
20   Information & Communication                 No     27       62.79
21   Information & Communication  Prefer not to say      2        4.65
22   Information & Communication                Yes     14       32.56
23                  Motor Trades                 No      2       50.00
24                  Motor Trades                Yes      2       50.00
25                    Production                 No     33       80.49
26                    Production  Prefer not to say      1        2.44
27                    Production                Yes      7       17.07
28      Professional & Technical                 No     46       86.79
29      Professional & Technical  Prefer not to say      1        1.89
30      Professional & Technical                Yes      6       11.32
31                      Property                 No     10       90.91
32                      Property                Yes      1        9.09
33        Public Admin & Defence                 No     47       72.31
34        Public Admin & Defence  Prefer not to say      3        4.62
35        Public Admin & Defence                Yes     15       23.08
36                        Retail                 No     53       79.10
37                        Retail  Prefer not to say      1        1.49
38                        Retail                Yes     13       19.40
39           Transport & Storage                 No     23       85.19
40           Tra
... [output truncated]
```

```text
<Figure size 1000x400 with 1 Axes>
```

## Cell 229 — markdown

### Gender × Age group → All indexes

## Cell 230 — code

```python
gender_age_index_summary = (
    df
    .groupby(
        ["gender_labeled", "age_group_labeled"],
        as_index=False,
        observed=True
    )
    .agg(
        ethical_acceptability_mean=("ethical_acceptability_index", "mean"),
        ethical_culture_mean=("ethical_culture_index", "mean"),
        rule_tolerance_mean=("rule_tolerance_index", "mean"),
        future_ethics_concern_mean=("future_ethics_concern_index", "mean"),
        count=("ethical_acceptability_index", "count")
    )
    .dropna(subset=["gender_labeled", "age_group_labeled"])
    .round(3)
    .sort_values(["gender_labeled", "age_group_labeled"])
)

print(gender_age_index_summary)
```

**Text output:**

```text
gender_labeled age_group_labeled  ethical_acceptability_mean  ethical_culture_mean  rule_tolerance_mean  future_ethics_concern_mean  count
0          Female             18–24                       2.571                 3.810                3.072                       2.859     46
1          Female             25–34                       2.302                 3.893                2.733                       2.984     64
2          Female             35–44                       2.155                 3.779                2.712                       2.948     57
3          Female             45–54                       2.047                 3.650                2.539                       2.807     61
4          Female             55–64                       1.844                 3.622                2.643                       2.929     56
5          Female               65+                       1.771                 3.827                2.533                       3.000     20
6            Male             18–24                       2.638                 3.641                3.334                       2.917     50
7            Male             25–34                       2.532                 3.726                3.183                       3.149     66
8            Male             35–44                       2.474                 3.719                3.027                       2.994     66
9            Male             45–54                       2.282                 3.562                3.028                       3.085     79
10           Male             55–64                       2.012                 3.484                2.692                       2.953     61
11           Male               65+                       1.732                 3.884                2.752                       2.623     34
12          Other             25–34                       2.250                 2.786                2.200                       3.222      1
13          Other             35–44                       1.000                 4.214                1.200                       3.333      1
```

## Cell 231 — code

```python
# Reshape to long format
long_df = gender_age_index_summary.melt(
    id_vars=["gender_labeled", "age_group_labeled"],
    value_vars=[
        "ethical_acceptability_mean",
        "ethical_culture_mean",
        "rule_tolerance_mean",
        "future_ethics_concern_mean"
    ],
    var_name="Index",
    value_name="Mean Score"
)

# Cleaner labels
index_labels = {
    "ethical_acceptability_mean": "Ethical Acceptability",
    "ethical_culture_mean": "Ethical Culture",
    "rule_tolerance_mean": "Rule Tolerance",
    "future_ethics_concern_mean": "Future Ethics Concern"
}

long_df["Index"] = long_df["Index"].map(index_labels)

# Plot
g = sns.FacetGrid(
    long_df,
    col="Index",
    col_wrap=2,
    height=4,
    sharey=False
)

g.map_dataframe(
    sns.lineplot,
    x="age_group_labeled",
    y="Mean Score",
    hue="gender_labeled",
    marker="o"
)

g.add_legend(title="Gender")
g.set_axis_labels("Age Group", "Mean Index Score")
g.set_titles("{col_name}")

for ax in g.axes.flatten():
    ax.tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.show()
```

**Text output:**

```text
<Figure size 900.25x800 with 4 Axes>
```

## Cell 232 — code

```python
indexes = {
    "ethical_acceptability_mean": "Ethical Acceptability",
    "ethical_culture_mean": "Ethical Culture",
    "rule_tolerance_mean": "Rule Tolerance",
    "future_ethics_concern_mean": "Future Ethics Concern"
}

for col, title in indexes.items():
    pivot = gender_age_index_summary.pivot(
        index="gender_labeled",
        columns="age_group_labeled",
        values=col
    )

    plt.figure(figsize=(8, 4))
    sns.heatmap(
        pivot,
        annot=True,
        fmt=".2f",
        cmap="RdYlGn_r",
        cbar_kws={"label": "Mean Score"}
    )
    plt.title(f"{title} Index by Gender and Age Group",
              fontsize=13, fontweight="bold")
    plt.xlabel("Age Group")
    plt.ylabel("Gender")
    plt.tight_layout()
    plt.show()
```

**Text output:**

```text
<Figure size 800x400 with 2 Axes>
```

```text
<Figure size 800x400 with 2 Axes>
```

```text
<Figure size 800x400 with 2 Axes>
```

```text
<Figure size 800x400 with 2 Axes>
```
