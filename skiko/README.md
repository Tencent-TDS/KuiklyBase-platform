# Skiko

this patch is built on the official skiko version 0.7.97 to support the OpenHarmony and iOS platforms.

# How to Publish

## 1. Download skiko
First, clone the official skiko project locally:：

```
git clone https://github.com/JetBrains/skiko.git
```

Check out the 0.7.97 tag and create a branch：

```
git checkout v0.7.97 -b 0.7.97
```

## 2. apply patch

download patch to local, and apply it:

```
git apply skiko.patch
```

## 3. maven configuration

open `gradle.properties` , then config your upload maven url 、username、password

```
maven_publish_url=https://xxxx/repository/maven/xxx
maven_username=user_A
maven_password=password_A
```

and change your own skiko version
```
version=xxxx
```

## 4. publish skiko

after gradle sync, enter skiko' root path, execute `publish` ，publish skiko to your own maven
```
./gradlew :skiko:publish -Pdeploy.release=true  

```

# How to import

import skiko in `libs.version.toml`

```
skiko = "xxxx"

skikoCommon = { module = "org.jetbrains.skiko:skiko", version.ref = "skiko" }

```

and implementation in module's `build.gradle.kts`
```
implementation(libs.skikoCommon)
```
