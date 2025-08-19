# SkikoBridge

This project builds a bridge layer between Skia and OpenHarmony, enabling Skia-based graphics rendering capabilities.

# How to Publish

## 1. Initialize Project
```bash
mkdir SkikoBridge
cd SkikoBridge
git init
```

## 2. Apply Patch
```bash
git apply --allow-empty skiko-bridge.patch
```

## 3. Build Configuration

+ 1.Open the project in DevEco Studio
+ 2.Set build mode to `Release`
+ 3.Select the `skikobridge` module and execute:  `Build → Make Module 'skikobridge'`

# How to import

## 1. Obtain Artifact
Path to the HAR package:
```
skikobridge/build/default/outputs/default/skikobridge.har
```

## 2. Integrate into Application
Using compose-multiplatform-sample project as an example:

Copy `skikobridge.har` file to:
```
 compose-multiplatform-sample/harmonyApp/entry/libs
```