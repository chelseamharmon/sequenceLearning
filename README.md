# Sequence Learning Task 
The goal of this study is to investigate how caregiving related early adversity (crEA) exposure influences implicit motor sequence learning in school age children (6-12 years old) compared to a group of comparison children with no crEA exposure.

# Important Notes 
First subject ran March 18, 2018 (34 subjects) 
Switched to Touchscreen Version June 12, 2018

Subjects data from June 15, 2018 - June 22, 2018 Sequence was wrong on new version (sequence, random, random, sequence, i.e. do not use PA098 PA127 PA136 PA086, PA089) 

Subjects were removed when adding demographic data for having incorrect demographic data/experimenter error/insufficent collection (PA227, PA228, PA229)

01.21.2019 - changed the recognition slides to be 1 3 2 4 4 2 3 4 - instead of former 1 3 2 4 4 3 2 4 


Additional Authors: Harmon, C., Bloom, P., Fields, A., VanTieghem, M., Choy, T., Camacho, N., Gibson, L., Umbach, R., Heleniak, C., Tottenham, N.

# Data Cleaning 
see dataCleaning01.27.2022.Rmd (see below - shows how inputs were created from raw data) - takes inputs pre_touchscreen.task.data_11.16.21.csv and post_touchscreen.task.data_11.16.21.csv and cleans filed - outputs:
dataPostTouchCleaned1.28.2022.csv
questionnaireDataPostTouchCleaned1.28.2022.csv
dataPreTouchCleaned1.28.2022.csv
questionnaireDataPretTouchCleaned1.28.2022.csv


# Getting demographic data and Plottinng 
(see SequenceFixingDemographicsAndModelsCorrectBlock1.19.2022.Rmd for Frequentist models before prospectus and sequencePlottingAndAnalyses01.27.2022.Rmd for set up of Bayesian models after prospectus) 


On elvis, lab server 
can also run Rscript bayesModel1.R
```.R
{r}
library(dplyr)
library(brms)
library(bmlm)

taskData <- read.csv("allTaskDataCleaned_withDemo1.28.2022.csv")

head(taskData)
taskData$GroupBinary <- ifelse(taskData$GROUP=="C", 0, 1)
#names(taskData)
taskData$AgeMeanCentered <- taskData$Age - mean(taskData$Age)
mean(taskData$AgeMeanCentered)


#taskData %>% 
#  mutate(scale(Age, center=T, scale=FALSE))

taskData <- taskData %>%
  mutate(AgeMeanCenter = mean(Age, na.rm=T)) %>%
  mutate(AgeMeanCentered = Age - AgeMeanCenter)



brms_1 <- brm(responseTimeCorrect ~ GroupBinary + 
                DEM_3_GENDER_CHILD + #controlling for Gender
                AgeMeanCentered + #controlling for age 
                Block + 
                Block*GroupBinary + 
                (Block|participant), 
              data=taskData,
              seed=111)
summary(brms_1)

save(brms_1, file = "brms_1.RData")
```

#Plotting the model predictions

```.R
{r}
pred.data <- NULL 

for (i in unique(taskData$participant)){
  predict.Block <- data.frame(
    Block = c("Block1", "Block2", "Block3", "Block4"), 
    participant=i)
  pred.data <- rbind(pred.data, predict.Block)
}

head(pred.data)

pred.data.fill <- cbind(pred.data, fitted(brms_1, re_formula=NULL))

```


