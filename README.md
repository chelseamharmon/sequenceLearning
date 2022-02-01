# Sequence Learning Task 
The goal of this study is to investigate how caregiving related early adversity (crEA) exposure influences implicit motor sequence learning in school age children (6-12 years old) compared to a group of comparison children with no crEA exposure.

# Important Notes 
First subject ran March 18, 2018 (34 subjects) 
Switched to Touchscreen Version June 12, 2018

Subjects data from June 15, 2018 - June 20, 2018 Sequence was wrong on new version (sequence, random, random, sequence, i.e. do not use PA098 PA127 PA136 PA086) 

Subjects were removed when adding demographic data for having incorrect demographic data/experimenter error/insufficent collection (PA227, PA228, PA229)

01.21.2019 - changed the recognition slides to be 1 3 2 4 4 2 3 4 - instead of former 1 3 2 4 4 3 2 4 


Additional Authors: Harmon, C., Bloom, P., Fields, A., VanTieghem, M., Choy, T., Camacho, N., Gibson, L., Umbach, R., Heleniak, C., Tottenham, N.

# Data Cleaning 
run dataCleaning01.27.2022.Rmd (shows how inputs were created from raw data) - takes inputs pre_touchscreen.task.data_11.16.21.csv and post_touchscreen.task.data_11.16.21.csv and cleans filed - outputs:
dataPostTouchCleaned1.28.2022.csv
questionnaireDataPostTouchCleaned1.28.2022.csv
dataPreTouchCleaned1.28.2022.csv
questionnaireDataPretTouchCleaned1.28.2022.csv

```.R
```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
library(knitr)
library(tidyverse)
library(broom)
library(ggplot2)
library(plyr)
library(dplyr)
library(tidyr)
knitr::opts_chunk$set(echo = T, cache = F, tidy = F, warning = F, message = F)  # Code not shown by default

# Set global ggplot theme
theme_set(theme_bw() + theme(panel.grid = element_blank(),
                             strip.text = element_blank(),
                             strip.background = element_blank(),
                             legend.position = "none"))

#Change path to /danl/PACCT/subject_data/task-data/V1W1/sequence and /danl/PACCT/subject_data/task-data/V2W2/sequence when looking on the server 
```

#Getting Data From data Folder output from Psychopy 

```{r,include=FALSE}

all.file.names <- list.files(path = "/Users/chelseaharmon/Dropbox/danlab/Tasks/motorSequenceLearning/sequenceLearning/data/V1W1", pattern = ".csv")
length(all.file.names)
#all.file.names
#517 files 

#write.table(all.file.names, file = "all.file.namesV1W1_11.17.21.txt", quote = F, row.names = F, col.names = F, sep = ",")

all.file.path.names <- 1:length(all.file.names)
for(i in 1:length(all.file.names)){all.file.path.names[i] <- paste("/Users/chelseaharmon/Dropbox/danlab/Tasks/motorSequenceLearning/sequenceLearning/data/V1W1/",all.file.names[i], sep='')
}

#write.table(all.file.path.names, file = "all.file.pathsV1W1_11.17.21.txt", quote = F, row.names = F, col.names = F, sep = ",")

data.list.all <- list()
length(all.file.path.names)


for(i in 1:length(all.file.path.names)){
# assign data frame for each csv file and save it in the list of dataframes.
data.list.all[[i]] <- data.frame(read.csv(all.file.path.names[i], stringsAsFactors=T))
}

all.subject.list <- substr(all.file.names, start=1, stop=5)


#finding the biggest file output 
finding.longest.file <- data.frame(1:length(data.list.all))
for(i in 1:length(data.list.all)){
  finding.longest.file[i, 1] <- (all.subject.list[i])
  finding.longest.file[i, 2] <- (all.file.names[i])
  finding.longest.file[i, 3] <- (length(data.list.all[[i]]$participant))}


finding.longest.file <- 
  finding.longest.file[
  order(finding.longest.file[,1], -finding.longest.file[,3]),
]

use.these.data.files <- finding.longest.file[!duplicated(finding.longest.file$X1.length.data.list.),2]
W1.subject.list <- substr(use.these.data.files, start=1, stop=5)
length(W1.subject.list)
#(W1.subject.list)
#242

W1.use.these.data.files <- use.these.data.files

#write.table(W1.use.these.data.files, file = "file.namesV1W1_11.16.21.txt", quote = F, row.names = F, col.names = F, sep = ",")


W1.file.path.names <- 1:length(W1.use.these.data.files)
W1.file.path.names

for(i in 1:length(W1.use.these.data.files)){W1.file.path.names[i] <- paste("/Users/chelseaharmon/Dropbox/danlab/Tasks/motorSequenceLearning/sequenceLearning/data/V1W1/",use.these.data.files[i], sep='')
}

length(W1.file.path.names)

#write.table(W1.file.path.names, file = "file.pathsV1W1_11.17.21.txt", quote = F, row.names = F, col.names = F, sep = ",")

```

#Grabbing Wave 2 data 
```{r,include=FALSE}

W2.all.file.names <- list.files(path = "/Users/chelseaharmon/Dropbox/danlab/Tasks/motorSequenceLearning/sequenceLearning/data/V2W2", pattern = ".csv")
length(W2.all.file.names)
#101

#write.table(all.file.names, file = "all.file.namesV2W2_11.17.21.txt", quote = F, row.names = F, col.names = F, sep = ",")

W2.all.file.path.names <- 1:length(W2.all.file.names)
for(i in 1:length(W2.all.file.names)){W2.all.file.path.names[i] <- paste("/Users/chelseaharmon/Dropbox/danlab/Tasks/motorSequenceLearning/sequenceLearning/data/V2W2/",W2.all.file.names[i], sep='')
}

#write.table(all.file.path.names, file = "all.file.pathsV2W2_05.17.20.txt", quote = F, row.names = F, col.names = F, sep = ",")

W2.data.list.all <- list()

for(i in 1:length(W2.all.file.path.names)){
# assign data frame for each csv file and save it in the list of dataframes.
W2.data.list.all[[i]] <- data.frame(read.csv(W2.all.file.path.names[i], stringsAsFactors=T))
}

W2.all.subject.list <- substr(W2.all.file.names, start=1, stop=5)
length(W2.all.subject.list)

#finding the biggest file output 
W2.finding.longest.file <- data.frame(1:length(W2.data.list.all))
for(i in 1:length(W2.data.list.all)){
  W2.finding.longest.file[i, 1] <- (W2.all.subject.list[i])
  W2.finding.longest.file[i, 2] <- (W2.all.file.names[i])
  W2.finding.longest.file[i, 3] <- (length(W2.data.list.all[[i]]$participant))}


W2.finding.longest.file <- 
  W2.finding.longest.file[
  order(W2.finding.longest.file[,1], -W2.finding.longest.file[,3]),
]
head(W2.finding.longest.file)
W2.use.these.data.files <- W2.finding.longest.file[!duplicated(W2.finding.longest.file$X1.length.W2.data.list.),2]
#View(finding.longest.file)
W2.subject.list <- substr(W2.use.these.data.files, start=1, stop=5)
W2.subject.list
#W2.use.these.data.files
length(W2.subject.list)
#48

#write.table(W2.use.these.data.files, file = "file.namesV2W2_11.17.21.txt", quote = F, row.names = F, col.names = F, sep = ",")


W2.file.path.names <- 1:length(W2.use.these.data.files)
for(i in 1:length(W2.use.these.data.files)){W2.file.path.names[i] <- paste("/Users/chelseaharmon/Dropbox/danlab/Tasks/motorSequenceLearning/sequenceLearning/data/V2W2/",W2.use.these.data.files[i], sep='')
}
length(W2.file.path.names)

#write.table(W2.file.path.names, file = "file.pathsV2W2_11.16.21.txt", quote = F, row.names = F, col.names = F, sep = ",")
```


#Making sepearte csv with demographcis or W1 and W2 
```{r}
#wave 1
length(W1.file.path.names)
#242
taskData <- read.csv((W1.file.path.names[1]), stringsAsFactors = F)

W1.file.path.names <- W1.file.path.names[-1]
W1.use.these.data.files <- W1.use.these.data.files[-1]


for(i in 1:length(W1.file.path.names)){
  subData <- read.csv(W1.file.path.names[i])
  taskData <- plyr::rbind.fill(taskData, subData)
}


(unique(taskData$participant))



#renaming subjects who were mis-entered 
taskData$participant[taskData$participant=="PA101"] <- 101
taskData$participant[taskData$participant=="PA246"] <- 246
taskData$participant[taskData$participant=="PA325"] <- 325
taskData$participant[taskData$participant=="PA326"] <- 326
taskData$participant[taskData$participant=="PA246"] <- 246
#taskData$participant[taskData$participant=="PA008"] <- 8
#taskData$participant[taskData$participant=="PA010_V2W2"] <- 10
#taskData$participant[taskData$participant=="PA025"] <- 25
#taskData$participant[taskData$participant=="pa034"] <- 34
#taskData$participant[taskData$participant=="PA070_V2W2"] <- 70

write.csv(taskData, file= "Wave1RawData_12.03.21.csv", row.names = F)

```
