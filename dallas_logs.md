SEED = 35   # good for seatle - 15, portland - 35, austin - 47
# Define a sample city to analyze
CITY = "Dallas, TX, USA"
# Alternative cities to try: "Seattle, WA, USA", "Portland, OR, USA", "San Francisco, CA, USA", "Austin, TX, USA", "Los Angeles, CA, USA", "Chicago, IL, USA", "Dallas, TX, USA", "Houston, TX, USA"

POPULATION_POINTS = 500
# Budget constraint ($)
MAX_BUDGET = 1000000  # $1M budget for new stations
BASE_STATION_COST = 100000  # Cost per station

# Coverage parameters
MAX_COVERAGE_DISTANCE = 1000  # meters
MIN_DISTANCE_BETWEEN_STATIONS = 500  # meters

# Number of candidate locations to consider
NUM_CANDIDATE_LOCATIONS = 1000  



Starting EV charging station optimization for Dallas, TX, USA

=== COLLECTING DATA ===
Retrieved 36479 road network nodes and 92993 edges
Getting census data for specific counties: ['113']
Retrieved census data for 529 tracts
Generated 500 population points from road network as fallback
City bounds: -97.000482, 32.613216, -96.463632, 33.023937
Retrieved 73014 charging stations from NREL API within bounding box
Filtered to 232 stations actually within city boundary

=== GENERATING CANDIDATE LOCATIONS ===
Using all road nodes within city: 36274 nodes
Generated 1000 candidate locations avoiding water areas

=== PREPARING DATA FOR OPTIMIZATION ===
Preparing coverage matrix with visualization-consistent method...

  0%|          | 0/1000 [00:00<?, ?it/s]
  0%|          | 3/1000 [00:00<00:38, 25.97it/s]
  1%|          | 6/1000 [00:00<00:37, 26.77it/s]
  1%|          | 9/1000 [00:00<00:36, 26.96it/s]
  1%|1         | 12/1000 [00:00<00:36, 26.73it/s]
  2%|1         | 15/1000 [00:00<00:36, 27.27it/s]
  2%|1         | 18/1000 [00:00<00:35, 27.29it/s]
  2%|2         | 21/1000 [00:00<00:35, 27.24it/s]
  2%|2         | 24/1000 [00:00<00:35, 27.26it/s]
  3%|2         | 27/1000 [00:00<00:35, 27.27it/s]
  3%|3         | 30/1000 [00:01<00:36, 26.53it/s]
  3%|3         | 33/1000 [00:01<00:36, 26.37it/s]
  4%|3         | 36/1000 [00:01<00:35, 27.03it/s]
  4%|3         | 39/1000 [00:01<00:35, 27.09it/s]
  4%|4         | 42/1000 [00:01<00:35, 26.97it/s]
  4%|4         | 45/1000 [00:01<00:35, 27.25it/s]
  5%|4         | 49/1000 [00:01<00:33, 28.44it/s]
  5%|5         | 52/1000 [00:01<00:33, 28.10it/s]
  6%|5         | 55/1000 [00:02<00:33, 28.05it/s]
  6%|5         | 58/1000 [00:02<00:33, 28.20it/s]
  6%|6         | 61/1000 [00:02<00:34, 27.36it/s]
  6%|6         | 64/1000 [00:02<00:33, 27.89it/s]
  7%|6         | 67/1000 [00:02<00:33, 27.79it/s]
  7%|7         | 70/1000 [00:02<00:33, 27.73it/s]
  7%|7         | 73/1000 [00:02<00:33, 27.61it/s]
  8%|7         | 76/1000 [00:02<00:33, 27.33it/s]
  8%|7         | 79/1000 [00:02<00:33, 27.70it/s]
  8%|8         | 82/1000 [00:02<00:32, 28.15it/s]
  8%|8         | 85/1000 [00:03<00:32, 27.86it/s]
  9%|8         | 88/1000 [00:03<00:32, 28.28it/s]
  9%|9         | 91/1000 [00:03<00:33, 27.54it/s]
  9%|9         | 94/1000 [00:03<00:32, 28.07it/s]
 10%|9         | 97/1000 [00:03<00:32, 27.44it/s]
 10%|#         | 100/1000 [00:03<00:32, 27.79it/s]
 10%|#         | 103/1000 [00:03<00:31, 28.18it/s]
 11%|#         | 107/1000 [00:03<00:30, 29.22it/s]
 11%|#1        | 110/1000 [00:03<00:31, 28.71it/s]
 11%|#1        | 113/1000 [00:04<00:31, 28.28it/s]
 12%|#1        | 116/1000 [00:04<00:31, 28.24it/s]
 12%|#1        | 119/1000 [00:04<00:31, 27.69it/s]
 12%|#2        | 122/1000 [00:04<00:31, 27.59it/s]
 12%|#2        | 125/1000 [00:04<00:31, 28.05it/s]
 13%|#2        | 128/1000 [00:04<00:31, 28.03it/s]
 13%|#3        | 131/1000 [00:04<00:30, 28.17it/s]
 13%|#3        | 134/1000 [00:04<00:30, 28.31it/s]
 14%|#3        | 137/1000 [00:04<00:30, 28.56it/s]
 14%|#4        | 140/1000 [00:05<00:30, 28.30it/s]
 14%|#4        | 143/1000 [00:05<00:31, 27.48it/s]
 15%|#4        | 146/1000 [00:05<00:30, 27.98it/s]
 15%|#4        | 149/1000 [00:05<00:31, 27.04it/s]
 15%|#5        | 152/1000 [00:05<00:32, 26.38it/s]
 16%|#5        | 155/1000 [00:05<00:31, 26.47it/s]
 16%|#5        | 158/1000 [00:05<00:39, 21.11it/s]
 16%|#6        | 161/1000 [00:05<00:39, 21.47it/s]
 16%|#6        | 164/1000 [00:06<00:40, 20.83it/s]
 17%|#6        | 167/1000 [00:06<00:39, 21.02it/s]
 17%|#7        | 170/1000 [00:06<00:38, 21.58it/s]
 17%|#7        | 173/1000 [00:06<00:37, 22.00it/s]
 18%|#7        | 176/1000 [00:06<00:37, 22.24it/s]
 18%|#7        | 179/1000 [00:06<00:36, 22.22it/s]
 18%|#8        | 182/1000 [00:06<00:36, 22.55it/s]
 18%|#8        | 185/1000 [00:07<00:35, 22.99it/s]
 19%|#8        | 188/1000 [00:07<00:35, 23.01it/s]
 19%|#9        | 191/1000 [00:07<00:35, 22.89it/s]
 19%|#9        | 194/1000 [00:07<00:35, 22.83it/s]
 20%|#9        | 197/1000 [00:07<00:34, 23.18it/s]
 20%|##        | 200/1000 [00:07<00:33, 23.53it/s]
 20%|##        | 203/1000 [00:07<00:33, 24.11it/s]
 21%|##        | 206/1000 [00:07<00:34, 23.23it/s]
 21%|##        | 209/1000 [00:08<00:34, 23.19it/s]
 21%|##1       | 212/1000 [00:08<00:34, 23.01it/s]
 22%|##1       | 215/1000 [00:08<00:34, 23.03it/s]
 22%|##1       | 218/1000 [00:08<00:33, 23.05it/s]
 22%|##2       | 221/1000 [00:08<00:33, 23.20it/s]
 22%|##2       | 224/1000 [00:08<00:32, 23.71it/s]
 23%|##2       | 227/1000 [00:08<00:32, 23.76it/s]
 23%|##3       | 230/1000 [00:08<00:33, 23.31it/s]
 23%|##3       | 233/1000 [00:09<00:33, 23.19it/s]
 24%|##3       | 236/1000 [00:09<00:33, 23.12it/s]
 24%|##3       | 239/1000 [00:09<00:32, 23.74it/s]
 24%|##4       | 242/1000 [00:09<00:31, 24.11it/s]
 24%|##4       | 245/1000 [00:09<00:30, 24.38it/s]
 25%|##4       | 248/1000 [00:09<00:31, 24.21it/s]
 25%|##5       | 251/1000 [00:09<00:30, 24.69it/s]
 25%|##5       | 254/1000 [00:09<00:30, 24.78it/s]
 26%|##5       | 257/1000 [00:10<00:30, 24.20it/s]
 26%|##6       | 260/1000 [00:10<00:30, 24.00it/s]
 26%|##6       | 263/1000 [00:10<00:30, 24.17it/s]
 27%|##6       | 266/1000 [00:10<00:29, 24.51it/s]
 27%|##6       | 269/1000 [00:10<00:30, 23.93it/s]
 27%|##7       | 272/1000 [00:10<00:30, 24.15it/s]
 28%|##7       | 275/1000 [00:10<00:30, 24.07it/s]
 28%|##7       | 278/1000 [00:10<00:29, 24.17it/s]
 28%|##8       | 281/1000 [00:11<00:29, 24.42it/s]
 28%|##8       | 284/1000 [00:11<00:29, 24.13it/s]
 29%|##8       | 287/1000 [00:11<00:30, 23.75it/s]
 29%|##9       | 290/1000 [00:11<00:29, 24.10it/s]
 29%|##9       | 293/1000 [00:11<00:29, 23.77it/s]
 30%|##9       | 296/1000 [00:11<00:29, 24.22it/s]
 30%|##9       | 299/1000 [00:11<00:29, 23.78it/s]
 30%|###       | 302/1000 [00:11<00:29, 23.65it/s]
 30%|###       | 305/1000 [00:12<00:29, 23.48it/s]
 31%|###       | 308/1000 [00:12<00:29, 23.36it/s]
 31%|###1      | 311/1000 [00:12<00:29, 23.26it/s]
 31%|###1      | 314/1000 [00:12<00:29, 23.22it/s]
 32%|###1      | 317/1000 [00:12<00:29, 23.17it/s]
 32%|###2      | 320/1000 [00:12<00:30, 22.62it/s]
 32%|###2      | 323/1000 [00:12<00:33, 20.44it/s]
 33%|###2      | 326/1000 [00:13<00:33, 20.23it/s]
 33%|###2      | 329/1000 [00:13<00:36, 18.28it/s]
 33%|###3      | 331/1000 [00:13<00:36, 18.16it/s]
 33%|###3      | 333/1000 [00:13<00:36, 18.38it/s]
 34%|###3      | 336/1000 [00:13<00:34, 19.32it/s]
 34%|###3      | 338/1000 [00:13<00:34, 19.35it/s]
 34%|###4      | 340/1000 [00:13<00:34, 19.05it/s]
 34%|###4      | 342/1000 [00:13<00:34, 18.94it/s]
 34%|###4      | 344/1000 [00:14<00:36, 17.96it/s]
 35%|###4      | 346/1000 [00:14<00:35, 18.27it/s]
 35%|###4      | 348/1000 [00:14<00:35, 18.55it/s]
 35%|###5      | 351/1000 [00:14<00:32, 20.14it/s]
 35%|###5      | 354/1000 [00:14<00:32, 20.11it/s]
 36%|###5      | 357/1000 [00:14<00:31, 20.72it/s]
 36%|###6      | 360/1000 [00:14<00:37, 17.03it/s]
 36%|###6      | 362/1000 [00:15<00:36, 17.40it/s]
 36%|###6      | 364/1000 [00:15<00:35, 17.74it/s]
 37%|###6      | 366/1000 [00:15<00:35, 18.11it/s]
 37%|###6      | 369/1000 [00:15<00:32, 19.24it/s]
 37%|###7      | 372/1000 [00:15<00:31, 20.08it/s]
 38%|###7      | 375/1000 [00:15<00:30, 20.67it/s]
 38%|###7      | 378/1000 [00:15<00:29, 21.12it/s]
 38%|###8      | 381/1000 [00:15<00:28, 21.52it/s]
 38%|###8      | 384/1000 [00:16<00:28, 21.75it/s]
 39%|###8      | 387/1000 [00:16<00:27, 21.93it/s]
 39%|###9      | 390/1000 [00:16<00:27, 22.11it/s]
 39%|###9      | 393/1000 [00:16<00:27, 21.98it/s]
 40%|###9      | 396/1000 [00:16<00:27, 21.97it/s]
 40%|###9      | 399/1000 [00:16<00:27, 21.92it/s]
 40%|####      | 402/1000 [00:16<00:26, 22.25it/s]
 40%|####      | 405/1000 [00:17<00:26, 22.33it/s]
 41%|####      | 408/1000 [00:17<00:26, 22.17it/s]
 41%|####1     | 411/1000 [00:17<00:26, 22.42it/s]
 41%|####1     | 414/1000 [00:17<00:26, 22.31it/s]
 42%|####1     | 417/1000 [00:17<00:26, 22.39it/s]
 42%|####2     | 420/1000 [00:17<00:25, 22.38it/s]
 42%|####2     | 423/1000 [00:17<00:26, 21.86it/s]
 43%|####2     | 426/1000 [00:17<00:26, 21.69it/s]
 43%|####2     | 429/1000 [00:18<00:26, 21.74it/s]
 43%|####3     | 432/1000 [00:18<00:26, 21.82it/s]
 44%|####3     | 435/1000 [00:18<00:25, 21.86it/s]
 44%|####3     | 438/1000 [00:18<00:25, 21.97it/s]
 44%|####4     | 441/1000 [00:18<00:25, 21.63it/s]
 44%|####4     | 444/1000 [00:18<00:25, 21.75it/s]
 45%|####4     | 447/1000 [00:18<00:25, 21.71it/s]
 45%|####5     | 450/1000 [00:19<00:25, 21.79it/s]
 45%|####5     | 453/1000 [00:19<00:25, 21.87it/s]
 46%|####5     | 456/1000 [00:19<00:24, 21.91it/s]
 46%|####5     | 459/1000 [00:19<00:24, 22.09it/s]
 46%|####6     | 462/1000 [00:19<00:24, 22.28it/s]
 46%|####6     | 465/1000 [00:19<00:23, 22.53it/s]
 47%|####6     | 468/1000 [00:19<00:23, 22.56it/s]
 47%|####7     | 471/1000 [00:20<00:24, 21.99it/s]
 47%|####7     | 474/1000 [00:20<00:23, 21.93it/s]
 48%|####7     | 477/1000 [00:20<00:23, 21.95it/s]
 48%|####8     | 480/1000 [00:20<00:23, 22.14it/s]
 48%|####8     | 483/1000 [00:20<00:23, 22.17it/s]
 49%|####8     | 486/1000 [00:20<00:23, 21.91it/s]
 49%|####8     | 489/1000 [00:20<00:23, 22.10it/s]
 49%|####9     | 492/1000 [00:20<00:23, 22.05it/s]
 50%|####9     | 495/1000 [00:21<00:22, 22.00it/s]
 50%|####9     | 498/1000 [00:21<00:22, 22.11it/s]
 50%|#####     | 501/1000 [00:21<00:22, 22.07it/s]
 50%|#####     | 504/1000 [00:21<00:22, 22.24it/s]
 51%|#####     | 507/1000 [00:21<00:21, 22.58it/s]
 51%|#####1    | 510/1000 [00:21<00:21, 22.79it/s]
 51%|#####1    | 513/1000 [00:21<00:21, 22.97it/s]
 52%|#####1    | 516/1000 [00:22<00:21, 23.04it/s]
 52%|#####1    | 519/1000 [00:22<00:20, 22.95it/s]
 52%|#####2    | 522/1000 [00:22<00:21, 22.61it/s]
 52%|#####2    | 525/1000 [00:22<00:22, 21.42it/s]
 53%|#####2    | 528/1000 [00:22<00:23, 19.98it/s]
 53%|#####3    | 531/1000 [00:22<00:23, 19.68it/s]
 53%|#####3    | 534/1000 [00:22<00:23, 19.84it/s]
 54%|#####3    | 537/1000 [00:23<00:23, 19.88it/s]
 54%|#####4    | 540/1000 [00:23<00:22, 20.11it/s]
 54%|#####4    | 543/1000 [00:23<00:22, 20.07it/s]
 55%|#####4    | 546/1000 [00:23<00:21, 20.70it/s]
 55%|#####4    | 549/1000 [00:23<00:22, 20.39it/s]
 55%|#####5    | 552/1000 [00:23<00:21, 20.59it/s]
 56%|#####5    | 555/1000 [00:23<00:20, 21.48it/s]
 56%|#####5    | 558/1000 [00:24<00:20, 21.47it/s]
 56%|#####6    | 561/1000 [00:24<00:20, 21.43it/s]
 56%|#####6    | 564/1000 [00:24<00:20, 21.22it/s]
 57%|#####6    | 567/1000 [00:24<00:20, 21.06it/s]
 57%|#####6    | 570/1000 [00:24<00:19, 21.64it/s]
 57%|#####7    | 573/1000 [00:24<00:19, 22.04it/s]
 58%|#####7    | 576/1000 [00:24<00:19, 22.22it/s]
 58%|#####7    | 579/1000 [00:25<00:25, 16.34it/s]
 58%|#####8    | 581/1000 [00:25<00:26, 16.02it/s]
 58%|#####8    | 583/1000 [00:25<00:25, 16.54it/s]
 58%|#####8    | 585/1000 [00:25<00:24, 17.27it/s]
 59%|#####8    | 587/1000 [00:25<00:23, 17.91it/s]
 59%|#####8    | 590/1000 [00:25<00:21, 18.73it/s]
 59%|#####9    | 593/1000 [00:25<00:20, 19.90it/s]
 60%|#####9    | 596/1000 [00:26<00:19, 20.51it/s]
 60%|#####9    | 599/1000 [00:26<00:19, 20.90it/s]
 60%|######    | 602/1000 [00:26<00:18, 21.04it/s]
 60%|######    | 605/1000 [00:26<00:18, 21.69it/s]
 61%|######    | 608/1000 [00:26<00:21, 18.60it/s]
 61%|######1   | 610/1000 [00:26<00:20, 18.64it/s]
 61%|######1   | 613/1000 [00:26<00:19, 19.57it/s]
 62%|######1   | 616/1000 [00:27<00:19, 20.16it/s]
 62%|######1   | 619/1000 [00:27<00:18, 21.14it/s]
 62%|######2   | 622/1000 [00:27<00:17, 21.58it/s]
 62%|######2   | 625/1000 [00:27<00:16, 22.35it/s]
 63%|######2   | 628/1000 [00:27<00:15, 23.33it/s]
 63%|######3   | 631/1000 [00:27<00:15, 23.79it/s]
 63%|######3   | 634/1000 [00:27<00:15, 24.25it/s]
 64%|######3   | 637/1000 [00:27<00:14, 24.33it/s]
 64%|######4   | 640/1000 [00:28<00:14, 24.53it/s]
 64%|######4   | 643/1000 [00:28<00:14, 24.66it/s]
 65%|######4   | 646/1000 [00:28<00:14, 24.76it/s]
 65%|######4   | 649/1000 [00:28<00:14, 24.10it/s]
 65%|######5   | 652/1000 [00:28<00:14, 24.07it/s]
 66%|######5   | 655/1000 [00:28<00:14, 24.34it/s]
 66%|######5   | 658/1000 [00:28<00:13, 24.99it/s]
 66%|######6   | 661/1000 [00:28<00:13, 24.53it/s]
 66%|######6   | 664/1000 [00:29<00:13, 24.68it/s]
 67%|######6   | 667/1000 [00:29<00:13, 23.82it/s]
 67%|######7   | 670/1000 [00:29<00:14, 23.47it/s]
 67%|######7   | 673/1000 [00:29<00:13, 23.66it/s]
 68%|######7   | 676/1000 [00:29<00:13, 23.65it/s]
 68%|######7   | 679/1000 [00:29<00:13, 23.77it/s]
 68%|######8   | 682/1000 [00:29<00:13, 24.23it/s]
 68%|######8   | 685/1000 [00:29<00:13, 24.02it/s]
 69%|######8   | 688/1000 [00:30<00:13, 23.66it/s]
 69%|######9   | 691/1000 [00:30<00:13, 23.11it/s]
 69%|######9   | 694/1000 [00:30<00:13, 23.06it/s]
 70%|######9   | 697/1000 [00:30<00:13, 22.98it/s]
 70%|#######   | 700/1000 [00:30<00:13, 22.71it/s]
 70%|#######   | 703/1000 [00:30<00:13, 22.44it/s]
 71%|#######   | 706/1000 [00:30<00:13, 22.47it/s]
 71%|#######   | 709/1000 [00:30<00:12, 22.49it/s]
 71%|#######1  | 712/1000 [00:31<00:12, 22.73it/s]
 72%|#######1  | 715/1000 [00:31<00:12, 22.84it/s]
 72%|#######1  | 718/1000 [00:31<00:12, 22.91it/s]
 72%|#######2  | 721/1000 [00:31<00:12, 22.96it/s]
 72%|#######2  | 724/1000 [00:31<00:11, 23.10it/s]
 73%|#######2  | 727/1000 [00:31<00:11, 23.58it/s]
 73%|#######3  | 730/1000 [00:31<00:11, 23.94it/s]
 73%|#######3  | 733/1000 [00:31<00:11, 23.66it/s]
 74%|#######3  | 736/1000 [00:32<00:11, 23.88it/s]
 74%|#######3  | 739/1000 [00:32<00:10, 23.85it/s]
 74%|#######4  | 742/1000 [00:32<00:10, 23.91it/s]
 74%|#######4  | 745/1000 [00:32<00:10, 24.17it/s]
 75%|#######4  | 748/1000 [00:32<00:10, 24.21it/s]
 75%|#######5  | 751/1000 [00:32<00:10, 24.39it/s]
 75%|#######5  | 754/1000 [00:32<00:10, 24.22it/s]
 76%|#######5  | 757/1000 [00:32<00:10, 24.23it/s]
 76%|#######6  | 760/1000 [00:33<00:10, 23.68it/s]
 76%|#######6  | 763/1000 [00:33<00:09, 24.10it/s]
 77%|#######6  | 766/1000 [00:33<00:09, 24.13it/s]
 77%|#######6  | 769/1000 [00:33<00:09, 24.34it/s]
 77%|#######7  | 772/1000 [00:33<00:09, 24.31it/s]
 78%|#######7  | 775/1000 [00:33<00:09, 24.08it/s]
 78%|#######7  | 778/1000 [00:33<00:09, 24.26it/s]
 78%|#######8  | 781/1000 [00:33<00:09, 24.26it/s]
 78%|#######8  | 784/1000 [00:34<00:08, 24.27it/s]
 79%|#######8  | 787/1000 [00:34<00:08, 24.52it/s]
 79%|#######9  | 790/1000 [00:34<00:08, 23.96it/s]
 79%|#######9  | 793/1000 [00:34<00:08, 24.03it/s]
 80%|#######9  | 796/1000 [00:34<00:08, 24.24it/s]
 80%|#######9  | 799/1000 [00:34<00:08, 24.38it/s]
 80%|########  | 802/1000 [00:34<00:08, 24.54it/s]
 80%|########  | 805/1000 [00:34<00:07, 24.68it/s]
 81%|########  | 808/1000 [00:35<00:07, 24.43it/s]
 81%|########1 | 811/1000 [00:35<00:07, 24.03it/s]
 81%|########1 | 814/1000 [00:35<00:07, 24.12it/s]
 82%|########1 | 817/1000 [00:35<00:07, 24.16it/s]
 82%|########2 | 820/1000 [00:35<00:07, 23.33it/s]
 82%|########2 | 823/1000 [00:35<00:07, 23.45it/s]
 83%|########2 | 826/1000 [00:35<00:07, 24.04it/s]
 83%|########2 | 829/1000 [00:35<00:07, 22.92it/s]
 83%|########3 | 832/1000 [00:36<00:07, 23.05it/s]
 84%|########3 | 835/1000 [00:36<00:07, 23.38it/s]
 84%|########3 | 838/1000 [00:36<00:06, 23.43it/s]
 84%|########4 | 841/1000 [00:36<00:06, 23.61it/s]
 84%|########4 | 844/1000 [00:36<00:06, 23.94it/s]
 85%|########4 | 847/1000 [00:36<00:06, 23.92it/s]
 85%|########5 | 850/1000 [00:36<00:06, 23.62it/s]
 85%|########5 | 853/1000 [00:36<00:06, 23.76it/s]
 86%|########5 | 856/1000 [00:37<00:06, 23.78it/s]
 86%|########5 | 859/1000 [00:37<00:05, 23.73it/s]
 86%|########6 | 862/1000 [00:37<00:05, 23.54it/s]
 86%|########6 | 865/1000 [00:37<00:05, 23.53it/s]
 87%|########6 | 868/1000 [00:37<00:05, 23.38it/s]
 87%|########7 | 871/1000 [00:37<00:05, 23.51it/s]
 87%|########7 | 874/1000 [00:37<00:05, 23.80it/s]
 88%|########7 | 877/1000 [00:38<00:05, 23.80it/s]
 88%|########8 | 880/1000 [00:38<00:05, 23.85it/s]
 88%|########8 | 883/1000 [00:38<00:04, 24.24it/s]
 89%|########8 | 886/1000 [00:38<00:04, 24.20it/s]
 89%|########8 | 889/1000 [00:38<00:04, 24.37it/s]
 89%|########9 | 892/1000 [00:38<00:04, 24.31it/s]
 90%|########9 | 895/1000 [00:38<00:04, 23.99it/s]
 90%|########9 | 898/1000 [00:38<00:04, 24.18it/s]
 90%|######### | 901/1000 [00:38<00:04, 24.31it/s]
 90%|######### | 904/1000 [00:39<00:03, 24.30it/s]
 91%|######### | 907/1000 [00:39<00:03, 24.37it/s]
 91%|#########1| 910/1000 [00:39<00:03, 24.25it/s]
 91%|#########1| 913/1000 [00:39<00:03, 24.38it/s]
 92%|#########1| 916/1000 [00:39<00:03, 24.28it/s]
 92%|#########1| 919/1000 [00:39<00:03, 24.17it/s]
 92%|#########2| 922/1000 [00:39<00:03, 23.73it/s]
 92%|#########2| 925/1000 [00:40<00:03, 23.45it/s]
 93%|#########2| 928/1000 [00:40<00:03, 23.66it/s]
 93%|#########3| 931/1000 [00:40<00:02, 23.74it/s]
 93%|#########3| 934/1000 [00:40<00:02, 23.96it/s]
 94%|#########3| 937/1000 [00:40<00:02, 24.01it/s]
 94%|#########3| 940/1000 [00:40<00:02, 24.22it/s]
 94%|#########4| 943/1000 [00:40<00:02, 24.05it/s]
 95%|#########4| 946/1000 [00:40<00:02, 24.03it/s]
 95%|#########4| 949/1000 [00:40<00:02, 23.94it/s]
 95%|#########5| 952/1000 [00:41<00:02, 23.76it/s]
 96%|#########5| 955/1000 [00:41<00:02, 18.88it/s]
 96%|#########5| 958/1000 [00:41<00:02, 19.19it/s]
 96%|#########6| 961/1000 [00:41<00:01, 19.81it/s]
 96%|#########6| 964/1000 [00:41<00:01, 20.67it/s]
 97%|#########6| 967/1000 [00:41<00:01, 21.50it/s]
 97%|#########7| 970/1000 [00:42<00:01, 22.09it/s]
 97%|#########7| 973/1000 [00:42<00:01, 22.44it/s]
 98%|#########7| 976/1000 [00:42<00:01, 23.00it/s]
 98%|#########7| 979/1000 [00:42<00:00, 23.44it/s]
 98%|#########8| 982/1000 [00:42<00:00, 23.80it/s]
 98%|#########8| 985/1000 [00:42<00:00, 23.52it/s]
 99%|#########8| 988/1000 [00:42<00:00, 23.72it/s]
 99%|#########9| 991/1000 [00:42<00:00, 24.03it/s]
 99%|#########9| 994/1000 [00:43<00:00, 24.22it/s]
100%|#########9| 997/1000 [00:43<00:00, 24.03it/s]
100%|##########| 1000/1000 [00:43<00:00, 23.96it/s]
100%|##########| 1000/1000 [00:43<00:00, 23.10it/s]
Coverage matrix: (500, 1001) - should now match visualization!

=== RUNNING OPTIMIZATION ===

=== STARTING MILP OPTIMIZATION ===
Population points: 500
Candidate locations: 1000
Total population: 2,606,500
Station costs range: $50,094 - $149,905
Added 441 coverage constraints
Solving MILP problem...
Welcome to the CBC MILP Solver 
Version: 2.10.3 
Build Date: Dec 15 2019 

command line - C:\Users\Darya\AppData\Local\Programs\Python\Python311\Lib\site-packages\pulp\apis\../solverdir/cbc/win/i64/cbc.exe C:\Users\Darya\AppData\Local\Temp\ab7872ae2fa24bb0acbb56173f1281ec-pulp.mps -max -timeMode elapsed -branch -printingOptions all -solution C:\Users\Darya\AppData\Local\Temp\ab7872ae2fa24bb0acbb56173f1281ec-pulp.sol (default strategy 1)
At line 2 NAME          MODEL
At line 3 ROWS
At line 506 COLUMNS
At line 7067 RHS
At line 7569 BOUNDS
At line 9070 ENDATA
Problem MODEL has 501 rows, 1500 columns and 3060 elements
Coin0008I MODEL read with 0 errors
Option for timeMode changed from cpu to elapsed
Continuous objective value is 444526 - 0.01 seconds
Cgl0002I 59 variables fixed
Cgl0004I processed model has 365 rows, 1111 columns (1111 integer (1111 of which binary)) and 2594 elements
Cutoff increment increased from 1e-05 to 5213
Cbc0038I Initial state - 4 integers unsatisfied sum - 0.970002
Cbc0038I Pass   1: suminf.    0.83124 (4) obj. -442901 iterations 262
Cbc0038I Solution found of -422253
Cbc0038I Before mini branch and bound, 1103 integers at bound fixed and 0 continuous
Cbc0038I Full problem 365 rows 1111 columns, reduced to 1 rows 2 columns
Cbc0038I Mini branch and bound improved solution from -422253 to -432679 (0.04 seconds)
Cbc0038I Round again with cutoff of -438555
Cbc0038I Reduced cost fixing fixed 660 variables on major pass 2
Cbc0038I Pass   2: suminf.    0.83124 (4) obj. -442901 iterations 0
Cbc0038I Pass   3: suminf.    2.01820 (5) obj. -438555 iterations 276
Cbc0038I Pass   4: suminf.    0.83124 (4) obj. -442901 iterations 268
Cbc0038I Pass   5: suminf.    3.14745 (8) obj. -438555 iterations 277
Cbc0038I Pass   6: suminf.    3.03312 (7) obj. -438555 iterations 25
Cbc0038I Pass   7: suminf.    0.99755 (5) obj. -438555 iterations 25
Cbc0038I Pass   8: suminf.    0.90531 (8) obj. -438555 iterations 261
Cbc0038I Pass   9: suminf.    1.32703 (5) obj. -438555 iterations 283
Cbc0038I Pass  10: suminf.    0.40045 (1) obj. -442055 iterations 252
Cbc0038I Pass  11: suminf.    0.37575 (1) obj. -438555 iterations 23
Cbc0038I Pass  12: suminf.    1.73778 (4) obj. -438555 iterations 185
Cbc0038I Pass  13: suminf.    1.73778 (4) obj. -438555 iterations 32
Cbc0038I Pass  14: suminf.    1.21958 (9) obj. -438555 iterations 121
Cbc0038I Pass  15: suminf.    0.65812 (7) obj. -438555 iterations 21
Cbc0038I Pass  16: suminf.    2.52927 (6) obj. -443667 iterations 268
Cbc0038I Pass  17: suminf.    1.87275 (7) obj. -438555 iterations 258
Cbc0038I Pass  18: suminf.    1.30526 (3) obj. -441514 iterations 257
Cbc0038I Pass  19: suminf.    0.37575 (1) obj. -438555 iterations 48
Cbc0038I Pass  20: suminf.    0.40045 (1) obj. -442055 iterations 25
Cbc0038I Pass  21: suminf.    2.60408 (9) obj. -438555 iterations 280
Cbc0038I Pass  22: suminf.    1.48080 (5) obj. -438555 iterations 26
Cbc0038I Pass  23: suminf.    0.99346 (4) obj. -441844 iterations 268
Cbc0038I Pass  24: suminf.    0.99346 (4) obj. -441844 iterations 0
Cbc0038I Pass  25: suminf.    2.13582 (5) obj. -438555 iterations 279
Cbc0038I Pass  26: suminf.    2.86991 (8) obj. -438555 iterations 25
Cbc0038I Pass  27: suminf.    2.13582 (5) obj. -438555 iterations 25
Cbc0038I Pass  28: suminf.    1.69875 (10) obj. -438555 iterations 36
Cbc0038I Pass  29: suminf.    0.04242 (1) obj. -438555 iterations 309
Cbc0038I Pass  30: suminf.    0.06712 (1) obj. -438942 iterations 27
Cbc0038I Pass  31: suminf.    1.58971 (10) obj. -438555 iterations 297
Cbc0038I Rounding solution of -437892 is better than previous of -432679

Cbc0038I Before mini branch and bound, 1052 integers at bound fixed and 0 continuous
Cbc0038I Full problem 365 rows 1111 columns, reduced to 1 rows 3 columns
Cbc0038I Mini branch and bound did not improve solution (0.11 seconds)
Cbc0038I Round again with cutoff of -443389
Cbc0038I Reduced cost fixing fixed 751 variables on major pass 3
Cbc0038I Pass  31: suminf.    0.97000 (4) obj. -444526 iterations 9
Cbc0038I Pass  32: suminf.    2.48659 (7) obj. -443389 iterations 307
Cbc0038I Pass  33: suminf.    2.17236 (5) obj. -444471 iterations 268
Cbc0038I Pass  34: suminf.    2.17236 (5) obj. -444471 iterations 1
Cbc0038I Pass  35: suminf.    2.37997 (6) obj. -443389 iterations 233
Cbc0038I Pass  36: suminf.    2.17236 (5) obj. -444471 iterations 232
Cbc0038I Pass  37: suminf.    2.66856 (8) obj. -443389 iterations 237
Cbc0038I Pass  38: suminf.    2.37997 (6) obj. -443389 iterations 16
Cbc0038I Pass  39: suminf.    2.37997 (6) obj. -443389 iterations 10
Cbc0038I Pass  40: suminf.    1.18800 (5) obj. -443389 iterations 17
Cbc0038I Pass  41: suminf.    0.97000 (4) obj. -444526 iterations 252
Cbc0038I Pass  42: suminf.    2.48659 (7) obj. -443389 iterations 283
Cbc0038I Pass  43: suminf.    2.17236 (5) obj. -444471 iterations 265
Cbc0038I Pass  44: suminf.    2.18569 (7) obj. -443389 iterations 268
Cbc0038I Pass  45: suminf.    1.18800 (5) obj. -443389 iterations 86
Cbc0038I Pass  46: suminf.    1.18800 (5) obj. -443389 iterations 52
Cbc0038I Pass  47: suminf.    1.18800 (5) obj. -443389 iterations 60
Cbc0038I Pass  48: suminf.    1.18800 (5) obj. -443389 iterations 44
Cbc0038I Pass  49: suminf.    1.18800 (5) obj. -443389 iterations 18
Cbc0038I Pass  50: suminf.    2.18569 (7) obj. -443389 iterations 19
Cbc0038I Pass  51: suminf.    1.18800 (5) obj. -443389 iterations 14
Cbc0038I Pass  52: suminf.    1.18800 (5) obj. -443389 iterations 20
Cbc0038I Pass  53: suminf.    1.18800 (5) obj. -443389 iterations 40
Cbc0038I Pass  54: suminf.    2.18569 (7) obj. -443389 iterations 17
Cbc0038I Pass  55: suminf.    1.18800 (5) obj. -443389 iterations 25
Cbc0038I Pass  56: suminf.    2.64786 (8) obj. -443389 iterations 41
Cbc0038I Pass  57: suminf.    2.37997 (6) obj. -443389 iterations 28
Cbc0038I Pass  58: suminf.    2.64786 (8) obj. -443389 iterations 22
Cbc0038I Pass  59: suminf.    2.37997 (6) obj. -443389 iterations 24
Cbc0038I Pass  60: suminf.    2.64702 (7) obj. -443389 iterations 25
Cbc0038I No solution found this major pass
Cbc0038I Before mini branch and bound, 1081 integers at bound fixed and 0 continuous
Cbc0038I Full problem 365 rows 1111 columns, reduced to 1 rows 2 columns
Cbc0038I Mini branch and bound did not improve solution (0.18 seconds)
Cbc0038I After 0.18 seconds - Feasibility pump exiting with objective of -437892 - took 0.15 seconds
Cbc0012I Integer solution of -437892 found by feasibility pump after 0 iterations and 0 nodes (0.18 seconds)
Cbc0038I Full problem 365 rows 1111 columns, reduced to 1 rows 2 columns
Cbc0013I At root node, 0 cuts changed objective from -444525.53 to -444525.53 in 1 passes
Cbc0014I Cut generator 0 (Probing) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 1 (Gomory) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.006 seconds - new frequency is -100
Cbc0014I Cut generator 2 (Knapsack) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.001 seconds - new frequency is -100
Cbc0014I Cut generator 3 (Clique) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.002 seconds - new frequency is -100
Cbc0014I Cut generator 4 (MixedIntegerRounding2) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 5 (FlowCover) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0001I Search completed - best objective -437892, took 18 iterations and 0 nodes (0.21 seconds)
Cbc0032I Strong branching done 2 times (19 iterations), fathomed 1 nodes and fixed 0 variables
Cbc0035I Maximum depth 0, 743 variables fixed on reduced cost
Cuts at root node changed objective from -444526 to -435206
Probing was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Gomory was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.006 seconds)
Knapsack was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.001 seconds)
Clique was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.002 seconds)
MixedIntegerRounding2 was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
FlowCover was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
TwoMirCuts was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.001 seconds)
ZeroHalf was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.002 seconds)

Result - Optimal solution found

Objective value:                437892.00000000
Enumerated nodes:               0
Total iterations:               18
Time (CPU seconds):             0.22
Time (Wallclock seconds):       0.22

Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.25   (Wallclock seconds):       0.25

Optimization Status: Optimal
Selected 18 locations: ['L21', 'L84', 'L132', 'L138', 'L198', 'L207', 'L278', 'L335', 'L397', 'L436', 'L464', 'L634', 'L749', 'L750', 'L776', 'L807', 'L889', 'L990']

=== DETAILED STATION ANALYSIS ===

Station L21:
  Cost: $52,521
  Covers 4 population points
  Total population covered: 20,852
  Population points covered: [82013453, 81789277, 81738117, 82013538]

Station L84:
  Cost: $59,816
  Covers 4 population points
  Total population covered: 20,852
  Population points covered: [81803210, 82016795, 81661977, 81998958]

Station L132:
  Cost: $64,767
  Covers 6 population points
  Total population covered: 31,278
  Population points covered: [81791786, 81707521, 81721320, 81682311, 81814930, 81791776]

Station L138:
  Cost: $50,141
  Covers 8 population points
  Total population covered: 41,704
  Population points covered: [9002905915, 81759419, 82087950, 5393368878, 5393368882, 81936953, 81759273, 81676642]

Station L198:
  Cost: $57,118
  Covers 3 population points
  Total population covered: 15,639
  Population points covered: [81848142, 5409359950, 82100429]

Station L207:
  Cost: $54,321
  Covers 4 population points
  Total population covered: 20,852
  Population points covered: [81749602, 81788970, 81673808, 4470614031]

Station L278:
  Cost: $55,532
  Covers 4 population points
  Total population covered: 20,852
  Population points covered: [81786802, 81944713, 81574201, 81796117]

Station L335:
  Cost: $54,465
  Covers 3 population points
  Total population covered: 15,639
  Population points covered: [81746955, 81614391, 10675344803]

Station L397:
  Cost: $51,641
  Covers 4 population points
  Total population covered: 20,852
  Population points covered: [81692923, 81980515, 81848478, 81982032]

Station L436:
  Cost: $51,776
  Covers 4 population points
  Total population covered: 20,852
  Population points covered: [81699322, 82071264, 82050592, 82214102]

Station L464:
  Cost: $50,177
  Covers 4 population points
  Total population covered: 20,852
  Population points covered: [81683462, 2585146992, 81805825, 81762311]

Station L634:
  Cost: $51,738
  Covers 4 population points
  Total population covered: 20,852
  Population points covered: [5409885331, 81884713, 81816109, 81567943]

Station L749:
  Cost: $51,096
  Covers 4 population points
  Total population covered: 20,852
  Population points covered: [82031146, 81972472, 82191875, 82191413]

Station L750:
  Cost: $58,659
  Covers 4 population points
  Total population covered: 20,852
  Population points covered: [81992213, 82013236, 81805368, 81805379]

Station L776:
  Cost: $53,195
  Covers 5 population points
  Total population covered: 26,065
  Population points covered: [81716120, 82216957, 81775366, 81760410, 82150835]

Station L807:
  Cost: $55,098
  Covers 4 population points
  Total population covered: 20,852
  Population points covered: [2418119491, 81681297, 82131808, 2418143967]

Station L889:
  Cost: $62,844
  Covers 10 population points
  Total population covered: 52,130
  Population points covered: [81975110, 81900541, 81791164, 81719629, 81812686, 81841271, 82051144, 81795602, 82248278, 82180056]

Station L990:
  Cost: $60,685
  Covers 5 population points
  Total population covered: 26,065
  Population points covered: [81914907, 82017750, 81983584, 12873468564, 297226393]

=== POPULATION COVERAGE ANALYSIS ===
Creating detailed population coverage mapping...
Coverage mapping complete:
  - Points covered: 84/500 (16.8%)
  - Population covered: 437,892/2,606,500 (16.8%)

=== OPTIMIZATION RESULTS ===
Total budget: $1,000,000
Used budget: $995,590
Selected 18 locations
Covered population: 437,892 out of 2,606,500 (16.80%)

=== COVERAGE VALIDATION ===
Manual coverage calculation: 437,892 (16.80%)

=== CREATING VISUALIZATIONS ===
Creating visualization with accurate coverage display...
Calculating actual coverage for 500 population points...
Actual coverage calculation:
  - Points covered: 84/500 (16.8%)
  - Population covered: 437,892/2,606,500 (16.8%)
c:\Users\Darya\Desktop\Optimization_Project\vizualization.py:128: UserWarning: Legend does not support handles for PatchCollection instances.
See: https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html#implementing-a-custom-legend-handler
  plt.legend(fontsize=10, loc='upper right')
Calculating actual coverage for 500 population points...
Actual coverage calculation:
  - Points covered: 84/500 (16.8%)
  - Population covered: 437,892/2,606,500 (16.8%)
c:\Users\Darya\Desktop\Optimization_Project\vizualization.py:228: UserWarning: Geometry is in a geographic CRS. Results from 'centroid' are likely incorrect. Use 'GeoSeries.to_crs()' to re-project geometries to a projected CRS before this operation.

  city_center = city_gdf.centroid.iloc[0]
Interactive map saved as 'ev_charging_optimization_map_dallas.html'
Coverage statistics: 16.8% of population covered

=== OPTIMIZATION COMPLETE ===
Results: Selected 18 new charging station locations
Population coverage: 437892 out of 2606500 (16.80%)
Total cost: $995,590

[Done] exited with code=0 in 245.857 seconds
