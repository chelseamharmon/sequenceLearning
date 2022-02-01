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
run dataCleaning01.27.2022.Rmd (see below - shows how inputs were created from raw data) - takes inputs pre_touchscreen.task.data_11.16.21.csv and post_touchscreen.task.data_11.16.21.csv and cleans filed - outputs:
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

```.R
{r,include=FALSE}

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
```.R
{r,include=FALSE}

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
```.R
{r}
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


#Making csv with all subjects data

```.R
{r, include=FALSE}
#Because thius was run aleady we can load the data at the bottom of this code chunk 
#
# #taskData1 <- read.csv((file.path.names[1]), stringsAsFactors = F)
# 
# #file.path.names[1]
# #taskData <- read.csv((file.path.names[1]), stringsAsFactors = F)
# all.use.these.data.files <- c(W1.use.these.data.files,W2.use.these.data.files)
# 
# #write.table(all.use.these.data.files, file = "all.file.names_11.16.21.txt", quote = F, row.names = F, col.names = F, sep = ",")
# (all.use.these.data.files)
# length(W1.use.these.data.files) 
# length(W2.use.these.data.files)
# 
# 242+48
# 
# both.waves.file.path.name <- c(W1.file.path.names, W2.file.path.names)
# #write.table(both.waves.file.path.name, file = "all.file.paths_11.16.21.txt", quote = F, row.names = F, col.names = F, sep = ",")
# 
# length(both.waves.file.path.name)
# 
# #write.table(both.waves.file.path.name, file = "both.waves.file.paths_11.16.21.txt", quote = F, row.names = F, col.names = F, sep = ",")
# 
# taskData <- read.csv((both.waves.file.path.name[1]), stringsAsFactors = F)
# 
# both.waves.file.path.name <- both.waves.file.path.name[-1]
# all.use.these.data.files <- all.use.these.data.files[-1]
# 
# 
# #dirTask <- "/Users/chelseaharmon/Dropbox/danlab/Tasks/motorSequenceLearning/sequenceLearning/data/V1W1/"
# #use.these.data.files <- use.these.data.files[-1]
# all.use.these.data.files
# both.waves.file.path.name
# 
# 
# for(i in 1:length(both.waves.file.path.name)){
#   subData <- read.csv(both.waves.file.path.name[i])
#   taskData <- plyr::rbind.fill(taskData, subData)
# }
# 
# 
# length(taskData)
# length(unique(taskData$participant))
# (unique(taskData$participant))
# (length(unique(taskData$participant)))
# 
#
##Renaming strangely named participants 
# taskData$participant[taskData$participant=="PA101"] <- 101
# taskData$participant[taskData$participant=="PA246"] <- 246
# taskData$participant[taskData$participant=="PA325"] <- 325
# taskData$participant[taskData$participant=="PA326"] <- 326
# taskData$participant[taskData$participant=="PA246"] <- 246
# taskData$participant[taskData$participant=="PA008"] <- 008
# taskData$participant[taskData$participant=="PA010_V2W2"] <- 010
# taskData$participant[taskData$participant=="PA025"] <- 025
# taskData$participant[taskData$participant=="pa034"] <- 034
# taskData$participant[taskData$participant=="PA070_V2W2"] <- 070
# 
# #repeated data PA006 PA031 PA058 PA059 PA060 PA061 PA069
# 
# names(taskData)

#write.csv(taskData, file= "all.subject.task.data_11.16.21.csv", row.names = F)
taskData <- read.csv("all.subject.task.data_11.16.21.csv")
length(unique(taskData$participant))

count(taskData$participant)

#View(taskData)
#IMPORTANT: Demographic data should be merged with subject data AFTER separating into block - In this script we seperate pre and post touch screen data into blocks - look at SequenceFixingDemographicsAndModelsCorrectBlock1.19.2022.Rmd for next step of adding demographics - 
```


#Seperatng touch screen 
```.R
{r}
#View(taskData[taskData$allowableKey=="['num_7', 'num_4', 'num_1', 'num_0']",])
#taskData$preTouchScreen <- ifelse(taskData$allowableKey=="['num_7', 'num_4', 'num_1', 'num_0']", 1, 0)
#taskData$expName

#unique(taskData$preTouchScreen)
#table(taskData$preTouchScreen, taskData$allowableKey)

#taskData$preTouchScreen <- 1
#taskData$preTouchScreen[is.na(taskData$correctLocation)] <- 1
#taskData$preTouchScreen[!is.na(taskData$correctLocation)] <- 0

#Filter out non usable data 
#Those that were run with incorrect order (sequence, random, random, sequence)
#PA098 PA127 PA136 PA086
#View(taskData)

taskData <- taskData[!taskData$participant=="98",]
taskData <- taskData[!taskData$participant=="127",]
taskData <- taskData[!taskData$participant=="136",]
taskData <- taskData[!taskData$participant=="86",]


length(unique(taskData$participant))


#Task Data Touch Screen seperate data frame - possibly save this for later 
#taskDataTouch <- taskData[complete.cases(taskData$correctLocation), ]
#taskDataTouchCheck <- taskData[taskData$preTouchScreen ==1,]

#unique(taskDataTouch$participant)
#unique(taskDataTouchCheck$participant)

unique(taskData$date)
taskData$date1 <- substr(taskData$date, start=1, stop=11)
taskData$date1 
taskData$date1 <- as.Date(taskData$date1, format = ("%Y_%b_%d"))
class(taskData$date1)

taskData$PreTouchByDate<- ifelse(taskData$date1 > "2018-06-12", 0, 1)
unique(taskData$participant)

unique(taskData$participant[taskData$PreTouchByDate==1])
unique(taskData$participant[taskData$PreTouchByDate==0])
length(unique(taskData$participant[taskData$PreTouchByDate==1]))
length(unique(taskData$participant[taskData$PreTouchByDate==0]))

taskDataTouch <- taskData[taskData$PreTouchByDate==1,]
taskData <- taskData[taskData$PreTouchByDate==0,]

(unique(taskDataTouch$participant))
length(unique(taskData$participant))
head(taskDataTouch)

#write.csv(taskData, file= "post_touchscreen.task.data_11.16.21.csv", row.names = F)
#write.csv(taskDataTouch, file= "pre_touchscreen.task.data_11.16.21.csv", row.names = F)

```


#Cleaning touch screen data 
```.R
{r}

#head(taskDataTouch)
#names(taskDataTouch)

#Making new file with quesitons 
#questionsResponsesTouch <- taskDataTouch[!complete.cases(taskDataTouch$stimulusPresent.t), ]
#taskDataTouch <- taskDataTouch[complete.cases(taskDataTouch$stimulusPresent.t), ]

#taskDataTouch$keyResponse <- as.character(taskDataTouch$key_resp_9.keys)
#taskDataTouch$keyResponseTimes <- as.character(taskDataTouch$key_resp_9.rt)

#unique(taskDataTouch)

#Touch screen columns 
#taskDataTouch <- subset(taskDataTouch, select=c('participant', 'date', 'stimulusPresent.t', 'responseTimeCorrect', 'responseTimeIncorrect', 'trialIncorrect', 'correctLocation', 'pressLoc', 'anticipatoryResponse', 'preTouchScreen')) #


#table(taskData$participant, taskData$correctLocation)
#table(taskData$participant, taskData$preTouchScreen)
#table(taskData$participant, taskData$preTouchScreen)

#unique(taskDataTouch$participant)
#unique(taskData$date)
#taskDataDateSep <- separate(data = taskData, col = date, into = c("Year", "Month", "Day", "Time"), sep = "\\_")
#taskDataDateSep$Year
#unique(taskDataAll$preTouchScreen)


#taskData$trialIncorrect[is.na(taskData$trialIncorrect)] <- 0
#taskData$anticipatoryResponse[is.na(taskData$anticipatoryResponse)] <- 0

#taskData$trialCorrect <- taskData$trialIncorrect + 1
#taskData$trialCorrect[taskData$trialCorrect==2] <- 0

```


#Cleaning pre touch screen data 

```.R
{r}
taskDataPreTouch <- read.csv("pre_touchscreen.task.data_11.16.21.csv")

(unique(taskDataPreTouch$repetitionNumber))



(unique(taskDataPreTouch$repeitionNumber))
#View(taskDataPreTouch)
unique(taskDataPreTouch$thisRepN)
#Pre Touch screen columns 

#Seperating out questionnaire data 
unique(taskDataPreTouch$trials_questions.thisRepN)
#taskDataPreTouch[taskDataPreTouch$trials_questions.thisRepN==0,]


questionnaireDataPreTouch<- taskDataPreTouch %>% 
  filter(taskDataPreTouch$trials_questions.thisRepN==0) %>% 
  subset(select=c('participant', 'date1', 'stimulusPresent.t', 'correctKey', 'keyRespCorrect', 'correctKeyPressNum', 'key_resp_9.rt', 'key_resp_9.keys', 'trialCorrect', 'repetitionNumber', 'anticipatoryResponse', 'PreTouchByDate', 'recallResponse', 'recallResponseTime', 'RecordAnswer.rt', 'RecordAnswer.keys', 'questionsResponses')) 


taskDataPreTouch <- taskDataPreTouch %>% 
  filter(taskDataPreTouch$stimulusPresent.t>0) %>% 
  subset(select=c('participant', 'date1', 'stimulusPresent.t', 'correctKey', 'keyRespCorrect', 'correctKeyPressNum', 'key_resp_9.rt', 'key_resp_9.keys', 'trialCorrect', 'repetitionNumber', 'anticipatoryResponse', 'PreTouchByDate')) #

write.csv(questionnaireDataPreTouch, "questionnaireDataPretTouchCleaned1.28.2022.csv", row.names=F)


```

#seperating data into blocks, pre touch screen 

```.R
{r}

unique(taskDataPreTouch$participant)[2]


length(unique(taskDataPreTouch$participant))

table(taskDataPreTouch$participant)

#for(i in 1:length(unique(taskDataPreTouch$participant))){
#  taskDataPreTouch$TrialNum <- 
#  taskDataPreTouch[taskDataPreTouch$participant==unique(taskDataPreTouch$participant)[2],]

#}


taskDataPreTouch$TrialNum <- sequence(rle(taskDataPreTouch$participant)$lengths)



#excluding incomplete data, excluding subjects 58 (for 2 blocks), 60 (for 1 block), 73 (for 1 block), 80 (for 2 blocks), 82 (for not completing 1 full block), 84 (for 1 block), 93 (for not completing block 3) = 7 subjects 
taskDataPreTouch$participant

taskDataPreTouch <- taskDataPreTouch %>% 
  filter(!participant %in% c(58, 60, 73, 80, 82, 84, 93))

#in group analyses is it okay to keep those who did not complete the task, or should we only complete full data? - ask Paul, statistical question 


unique(taskDataPreTouch$participant)
length(unique(taskDataPreTouch$participant))
unique(taskData$participant)

#repeated in pre and post touch screen - 6, 



```


#seperating pre touch screen into Blocks 
```.R
{r}

taskDataPreTouchBlocks1 <- taskDataPreTouch 
#taskDataPreTouchBlocks1$Group <-  taskDataPreTouchBlocks1$Trial

#Post Touch screen has sequence length 8 for 10 sequences per block 
taskDataPreTouchBlocks1$Group1 <- taskDataPreTouchBlocks1$TrialNum <= 80 #100 
taskDataPreTouchBlocks1$Group2 <- between(taskDataPreTouchBlocks1$Trial, 81, 160)  #101,  200 ) 
taskDataPreTouchBlocks1$Group3 <- between(taskDataPreTouchBlocks1$Trial, 161, 240) #201,  300 ) 
taskDataPreTouchBlocks1$Group4 <- between(taskDataPreTouchBlocks1$Trial, 241, 320)   #301,  400 ) 

taskDataPreTouchBlocks1$Group[taskDataPreTouchBlocks1$Group1 == TRUE] <- "Block1"
taskDataPreTouchBlocks1$Group[taskDataPreTouchBlocks1$Group2 == TRUE] <- "Block2"
taskDataPreTouchBlocks1$Group[taskDataPreTouchBlocks1$Group3 == TRUE] <- "Block3"
taskDataPreTouchBlocks1$Group[taskDataPreTouchBlocks1$Group4 == TRUE] <- "Block4"
Group <- taskDataPreTouchBlocks1$Group

taskDataPreTouch <- (cbind(taskDataPreTouch, Group))
head(taskDataPreTouch)
unique(taskDataPreTouch$Group)
names(taskDataPreTouch)

write.csv(taskDataPreTouch, "dataPreTouchCleaned1.28.2022.csv", row.names=F)
#write.csv(taskDataPreTouch, "dataPreTouchCleaned1.19.2022.csv", row.names=F)

table(taskDataPreTouch$participant, taskDataPreTouch$Group)

#What are anticipatory responses that are incorrect??? 

```



#Cleaning post touch screen data 
```.R
{r, include=FALSE}
taskData <- read.csv("post_touchscreen.task.data_11.16.21.csv")
head(taskData)

#Seperating out questionnaire data 
names(taskData)
#View(taskData)
unique(taskData$stimulusPresent.t)
unique(taskData$X)

#Check these - are they real pre touch data snuck into the post touch data.frame?
taskData[taskData$correctKey=="['num_4']",]


#questionnaireDataTouch<- taskData %>% 
#  filter(taskData$trials_questions.thisRepN==0) %>% 
#  subset(select=c('participant', 'date1', 'stimulusPresent.t', 'correctKey', 'keyRespCorrect', 'correctKeyPressNum', 'key_resp_9.rt', 'key_resp_9.keys', 'trialCorrect', #'repetitionNumber', 'anticipatoryResponse', 'PreTouchByDate', 'recallResponse', 'recallResponseTime', 'RecordAnswer.rt', 'RecordAnswer.keys', 'questionsResponses')) 

#Check question respones and RecordAnswer.keys - checking for if questoinnresponses are pre touchscreen data only (should not be in this data set)
questionnaireDataTouch<- taskData %>% 
  filter(taskData$trials_questions.thisRepN==0) %>% 
  subset(select=c('participant', 'date1', 'stimulusPresent.t', 'correctKey', 'keyRespCorrect', 'correctKeyPressNum', 'key_resp_9.rt', 'key_resp_9.keys', 'trialCorrect', 'repetitionNumber', 'anticipatoryResponse', 'PreTouchByDate', 'recallResponse', 'recallResponseTime', 'RecordAnswer.keys' ,'questionsResponses', 'trials_questions.thisRepN', 'trials_questions.thisTrialN', 'trials_questions.thisN',  'trials_test.thisRepN', 'trials_test.thisTrialN','trials_test.thisN', 'trials_test.thisIndex', 'trials_recogtest.thisRepN', 'trials_recogtest.thisTrialN', 'trials_recogtest.thisN', 'trials_recogtest.thisIndex', 'AnswerFinished.keys', 'AnswerFinished.rt','RecordAnswer.keys')) #' trials_questions.thisIndex')) 

#I don't think I care abou tthis so leave it out - RecordAnswer.rt - this is the time for each letter press for the open ended question - do you play an instrument 

#taskData <- taskData %>% 
#  filter(taskData$stimulusPresent.t>0) %>% 
#  subset(select=c('participant', 'date1', 'stimulusPresent.t', 'correctKey', 'keyRespCorrect', 'correctKeyPressNum', 'key_resp_9.rt', 'key_resp_9.keys', 'trialCorrect', #'repetitionNumber', 'anticipatoryResponse', 'PreTouchByDate')) #

taskData <- taskData %>% 
  filter(taskData$stimulusPresent.t>0) %>% 
  subset(select=c('participant', 'date1', 'stimulusPresent.t', 'correctKey', 'correctKeyPressNum', 'trials_3.thisTrialN','trials_3.thisIndex', 'trials_2.thisRepN', 'trials_2.thisTrialN', 'correctLocation', 'correctImage', 'trialCorrect', 'trials_2.thisN', 'trials_2.thisIndex',  'repetitionNumber', 'anticipatoryResponse', 'responseTimeCorrect', 'responseTimeIncorrect', 'pressLoc', 'trialIncorrect', 'session', 'correctKey.1', 'frameRate', 'PreTouchByDate')) #

#View(taskData)
unique(taskData$participant)

#These are post touch screen answers 
#taskData <- taskData %>% select(-c('responseTimeCorrect', 'responseTimeIncorrect', 'trialIncorrect', 'correctLocation', 'pressLoc', 'anticipatoryResponse', 'correctImage'))

subject75data <- taskData[(taskData$participant==75),]
#View(subject75data)
length(subject75data$repetitionNumber)

subject6data <- taskData[(taskData$participant==6),]
length(subject75data$repetitionNumber)

subject31data <- taskData[(taskData$participant==31),]
length(subject75data$repetitionNumber)

#table(taskData$participant, taskData$pawPatrol1) >337
#table(taskData$participant, taskData$pawPatrol1) 

#incomplete data subject numbers 45, 112, 236, 253, 259, 274, 311, 317 ??????????????????????????
#subjects who completed post touch screen twice 3, 31


write.csv(questionnaireDataTouch, "questionnaireDataPostTouchCleaned1.28.2022.csv", row.names=F)

```


#seperating data into Blocks 
```.R
{r}

taskData$repetitionNumber


taskData$TrialNum <- sequence(rle(taskData$participant)$lengths)

unique(taskData$TrialNum)


# taskDataNoOutliers <- taskData[taskData$responseTimeCorrect < 100,]
# 
# ggplot(data=taskDataNoOutliers, aes(TrialNum, responseTimeCorrect, group=participant, color=participant)) + 
#   geom_point() + 
#   geom_line()
# 
# summaryAllValues <- taskData %>% 
#   group_by(participant, Group) %>%
#   summarise_at(vars(trialCorrect), funs(mean(., na.rm=TRUE), sd(., na.rm=T),se=sd/sqrt(n())))
# 
# 337/4
# taskData$Block <-rep(1:8, length=nrow(x))
# 
# library(dplyr)
# taskData %>% 
#  group_by(participant) %>% 
#  mutate(Block= c(rep(1:8)))
# 
# 
# taskData %>% 
#   group_by(participant) %>% 
#   mutate(num_in_group=seq_along(repetitionNumber)) %>% 
#   as.data.frame
# 
# df %>%
#  group_by(cat) %>%
#  mutate(num = 1:n())
# taskDataBlocks1 <- ddply(taskData, .(participant), mutate, Trial = seq_along(repetitionNumber))


#taskData$Trial <- c(1:length(taskData$repetitionNumber))
#taskDataBlocks1 <- ddply(taskData, .(participant), mutate, Trial = seq_along(repetitionNumber))
taskDataBlocks1 <- taskData
#taskDataBlocks1$Group <-  taskDataBlocks1$Trial

#Post Touch screen has sequence length 8 for 10 sequences per block 
taskDataBlocks1$Group1 <- taskDataBlocks1$TrialNum <= 80 #100
taskDataBlocks1$Group2 <- between(taskDataBlocks1$Trial, 81, 160)  #101,  200 ) 
taskDataBlocks1$Group3 <- between(taskDataBlocks1$Trial, 161, 240) #201,  300 ) 
taskDataBlocks1$Group4 <- between(taskDataBlocks1$Trial, 241, 320)   #301,  400 ) 

taskDataBlocks1$Group[taskDataBlocks1$Group1 == TRUE] <- "Block1"
taskDataBlocks1$Group[taskDataBlocks1$Group2 == TRUE] <- "Block2"
taskDataBlocks1$Group[taskDataBlocks1$Group3 == TRUE] <- "Block3"
taskDataBlocks1$Group[taskDataBlocks1$Group4 == TRUE] <- "Block4"
Group <- taskDataBlocks1$Group

taskData <- (cbind(taskData, Group))
head(taskData)
unique(taskData$Group)
names(taskData)
length(unique(taskData$participant))

unique(taskData$participant)


#write.csv(taskData, "dataPostTouchCleaned1.28.2022.csv", row.names=F)
#write.csv(taskData, "dataPostTouchCleaned1.15.2019.csv", row.names=F)



table(taskData$participant, taskData$Group)

#What are anticipatory responses that are incorrect??? 
```




#Removing data for incomplete or repeated 
```.R
{r}
#Removing incomplete data 
taskData <- taskData[!taskData$participant=='112',] #2 blocks only 
taskData <- taskData[!taskData$participant=='253',] #has only 1 block
taskData <- taskData[!taskData$participant=='311',] #only 2 blocks
taskData <- taskData[!taskData$participant=='317',] #only did a few trials of block 1 

#Repeated subject pre and post touch screen == 6 
#Repeated subject post touch screen twice == 3, 31

taskData <- taskData[!taskData$participant=='6',] #just use pre touch screen data so remove from post touch screen data sheet 

unique(taskData[taskData$participant=='3',]$date) #on elvis has two dates of data April 21 2019 and June 27 2019 - V2W2 - dates close together - check data entry master to see when this subject came in 

#View(taskData[taskData$participant=='3',]) 
unique(taskData[taskData$participant=='31',]$date)

unique(taskData[taskData$participant=='33',]$date)
#View(taskData[taskData$participant=='33',])

names(taskData)

taskData %>% filter(participant=="3") %>%
  group_by(TrialNum) %>%
  summarise_at(vars(responseTimeCorrect),funs(mean(., na.rm=TRUE)))


taskDataSubj3 <- 
  taskData %>% filter(participant=="3")

taskDataSubj3
unique(taskDataSubj3$session)


taskDataSubj3$trialnumall <- 1:640
taskDataSubj3[1:320,]$trialnumall <- 0
taskDataSubj3[321:640,]$trialnumall <- 1
taskDataSubj3 %>% 
  group_by(trialnumall, Group) %>%
  summarise_at(vars(responseTimeCorrect),funs(mean(., na.rm=TRUE)))

#data was repeated 2x (they are the same) because there was an extra data collected o6/27/2019 where no data was actually collected. Here I am going to remove the repeated trials 321-640

taskDataSubj3 <- taskDataSubj3[taskDataSubj3$trialnumall==0,]
length(taskDataSubj3)
taskData <- taskData[!taskData$participant=='3',] 


taskDataSubj3 <- taskDataSubj3[,1:26]


table(taskData$participant, taskData$Group)

#Removing the repeated data for subject 31 
taskData %>% filter(participant=="31") %>%
  group_by(date1, Group) %>%
  summarise_at(vars(responseTimeCorrect),funs(mean(., na.rm=TRUE)))


taskData[taskData$participant==31,]$date1=="2019-06-07"

unique(taskData[taskData$date1=="2019-06-07",]$participant)

taskData<- taskData[!taskData$date1=="2019-06-07",] 

table(taskData$participant, taskData$Group)

taskData <- dplyr::rename(taskData, Block = Group)

write.csv(taskData, "dataPostTouchCleaned1.28.2022.csv", row.names=F)

table(taskDataPreTouch$participant, taskDataPreTouch$Group)
taskDataPreTouch <- dplyr::rename(taskDataPreTouch, Block = Group)

write.csv(taskDataPreTouch, "dataPreTouchCleaned1.28.2022.csv", row.names=F)

```



#Merging pre and post touch data 

```.R
{r}

#head(taskDataPreTouch)
taskDataPreTouch <- read.csv("dataPreTouchCleaned1.28.2022.csv")
taskData <-  read.csv("dataPostTouchCleaned1.28.2022.csv")

unique(taskData$participant)
unique(taskDataPreTouch$participant)

head(taskData)

unique(taskData$session)
#View(taskData[which(taskData$trialIncorrect==1),])

#Check who has two sessions - looks like participant 22 only has session 2 no session 1 - should be okay

taskData %>% 
  filter(participant==22) %>% 
  group_by(Block, session) %>%
  summarise_at(vars(responseTimeCorrect),funs(mean(., na.rm=TRUE)))

unique(taskData[which(taskData$session==2),]$participant)
unique(taskData$PreTouchByDate)
unique(taskDataPreTouch$PreTouchByDate)
```

```.R
{r}
head(taskDataPreTouch)
#taskDataPreTouch$key_resp_9.rt

#sapply(taskDataPreTouch$key_resp_9.rt, tail, 1)

#sapply(taskDataPreTouch$key_resp_9.rt[[2]], tail, 1)
#testing with 2 (length 2 response times) and testing with 35 (length 3 response times)
(strsplit(taskDataPreTouch$key_resp_9.rt, split = ","))[[2]]
gsub("^.*, |]", "", taskDataPreTouch$key_resp_9.rt[[2]]) #replace anything BEFORE the , with nothing and replace the last ']' with nothing
gsub("\\[|\\]|, .*", "", taskDataPreTouch$key_resp_9.rt[[2]]) #replace anything AFTER the , with nothing and replace the last ']' with nothing

#(strsplit(taskDataPreTouch$key_resp_9.rt, split = ","))[[35]]
#gsub("^.*, |]", "", taskDataPreTouch$key_resp_9.rt[[35]]) #replace anything before the , with nothing and replace the last ']' with nothing

taskDataPreTouch$responseTimeCorrect <- gsub("\\[|\\]|^.*, ", "", taskDataPreTouch$key_resp_9.rt)
taskDataPreTouch$trialIncorrect <- ifelse(taskDataPreTouch$trialCorrect==0, 1,NA)
taskDataPreTouch$responseTimeIncorrect <- ifelse(taskDataPreTouch$trialIncorrect==1, gsub("\\[|\\]|, .*", "", taskDataPreTouch$key_resp_9.rt), NA)
taskDataPreTouch

#taskDataAll <- 

taskDataSubset <- taskData %>%
  subset(select=c('participant', 'date1', 'stimulusPresent.t', 'repetitionNumber', 'anticipatoryResponse', 'responseTimeCorrect', 'responseTimeIncorrect', 'trialIncorrect', 'PreTouchByDate', 'TrialNum', 'Block')) #Taking out the informative variables of pressLoc and correctLocation which would come in handy if you wanted to verify that an incorrect press was outside of the dimensional location. May also be important for varifying anticipatory responsnes 
taskDataPreTouchSubset <- taskDataPreTouch %>%
  subset(select=c('participant', 'date1', 'stimulusPresent.t', 'repetitionNumber', 'anticipatoryResponse', 'responseTimeCorrect', 'responseTimeIncorrect', 'trialIncorrect', 'PreTouchByDate', 'TrialNum', 'Block'))

allTaskData<- rbind(taskDataSubset, taskDataPreTouchSubset)



write.csv(allTaskData, "allTaskDataCleaned1.28.2022.csv", row.names=F)

```


