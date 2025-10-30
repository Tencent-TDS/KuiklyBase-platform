# okio

This patch is built on the official okio version c43c9a61 to support platform OpenHarmony。

# How to publish

## 1. download okio
At first, clone offcial okio project in local:

```
git clone https://github.com/Kotlin/okio.git
```

checkout tag c43c9a61 and create branch:

```
git checkout -b 3.9.10-KBA-001 c43c9a61
```

## 2. apply patch

download patch to local, and apply it:

```
git apply okio.patch
```

## 3. maven configuration

open `gradle.properties` , then config your upload maven url 、username、password

```
maven_publish_url=https://xxxx/repository/maven/xxx
maven_username=user_A
maven_password=password_A
```

and change your own okio version
```
version=xxxx
```

## 4. publish okio

after gradle sync, enter okio project' root path, execute `publish` ，publish okio to your own maven
```
./gradlew publish
```

# How to import

import okio in `libs.version.toml`

```
okioVersion = "3.9.10-KBA-001"

lib-okio = { group = "com.squareup.okio", name = "okio", version.ref = "okioVersion" }
```

and implementation in module's `build.gradle.kts`
```
implementation(lib.okio)
```