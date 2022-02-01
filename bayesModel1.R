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