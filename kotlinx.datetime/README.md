# kotlinx.datetime

This patch is built on the official kotlinx.datetime version 0.6.0-RC.2 to support platform OpenHarmony。

# How to publish

## 1. download kotlinx.datetime
At first, clone offcial kotlin.datetime project in local:

```
git clone https://github.com/Kotlin/kotlinx.datetime.git
```

checkout tag 0.6.0-RC.2 and create branch:

```
git checkout -b v0.6.0-RC.2 0.6.0-RC.2
```

## 2. apply patch

download patch to local, and apply it:

```
git apply kotlinx-datetime.patch
```

## 3. maven configuration

open `gradle.properties` , then config your upload maven url 、username、password

```
maven_publish_url=https://xxxx/repository/maven/xxx
maven_username=user_A
maven_password=password_A
```

and change your own kotlinx.datetime version
```
version=xxxx
```

## 4. publish kotlinx.datetime

after gradle sync, enter kotlinx.datetime project' root path, execute `publish` ，publish kotlinx.datetime to your own maven
```
./gradlew publish
```

# How to import

import kotlinx.datetime in `libs.version.toml`

```
datetimeVersion = "0.6.0-RC.2-KBA-001"

lib-kotlin-datetime = { group = "org.jetbrains.kotlinx", name = "kotlinx-datetime", version.ref = "datetimeVersion" }
```

and implementation in module's `build.gradle.kts`
```
implementation(lib.kotlin.datetime)
```
# How to import in HarmonyOs

```
"dependencies": {
    "@kuiklybase/timezone":"0.0.1"
  }
// init
import "@kuiklybase/timezone" // Initialization is required; otherwise it will crash.
```

# Some important things on Android.

```
// The datetime library is not compatible with devices running lower API levels.
// To solve this issue, we introduced `com.jakewharton.threetenabp:threetenabp:1.4.7`.
// For Android, make sure to initialize it during app startup:        
AndroidThreeTen.init(application)
```

