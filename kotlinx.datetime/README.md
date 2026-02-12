# kotlinx.datetime

This patch is built on the official kotlinx.datetime version 0.6.0-RC.2 to support platform OpenHarmony.

## Quick Start

### 1. Add Maven Repository

Add the Tencent Maven repository in your project's `settings.gradle.kts`:

```kotlin
dependencyResolutionManagement {
    repositories {
        maven {
            url = uri("https://mirrors.tencent.com/nexus/repository/maven-tencent/")
        }
    }
}
```

### 2. Add Dependency

Add the dependency in your module's `build.gradle.kts`:

```kotlin
implementation("org.jetbrains.kotlinx:kotlinx-datetime:0.6.0-RC.2-KBA-003")
```

Specifically, if you want to use it on the HarmonyOS (OpenHarmony) platform, you need to add the dependency in `build.ohos.gradle.kts`:

```kotlin
implementation("org.jetbrains.kotlinx:kotlinx-datetime:0.6.0-RC.2-KBA-003")
```

---

## Platform-Specific Notes

### HarmonyOS (OpenHarmony)

Add the timezone dependency in your HarmonyOS project:

```json
"dependencies": {
    "@kuiklybase/timezone": "0.0.1"
}
```

Initialize it in your code (required, otherwise it will crash):

```typescript
import "@kuiklybase/timezone"
```

### Android

The datetime library is not compatible with devices running lower API levels. To solve this issue, we introduced `com.jakewharton.threetenabp:threetenabp:1.4.7`.

For Android, make sure to initialize it during app startup:

```kotlin
AndroidThreeTen.init(application)
```

---

## How to Publish

### 1. Download kotlinx.datetime

Clone the official kotlinx.datetime project locally:

```bash
git clone https://github.com/Kotlin/kotlinx-datetime.git
```

Checkout tag 0.6.0-RC.2 and create a new branch:

```bash
git checkout -b v0.6.0-RC.2 v0.6.0-RC.2
```

### 2. Apply Patch

Download the patch file to the project root directory and apply it:

```bash
git apply kotlinx-datetime.patch
```

### 3. Configure gradle.properties

Open `gradle.properties` file to configure the version number and Maven repository settings.

#### 3.1 Modify Version Number

Find and update the version property to your desired version:

```properties
version=0.6.0-RC.2-ohos-1.0.0
```

> **Note**: There is a hardcoded version in `core/build.gradle.kts` (line 20). If the version number does not take effect after modification, check the `core/build.gradle.kts` file and delete or comment out the hardcoded version:
>
> ```kotlin
> // Delete or comment out this line if it exists
> version = "0.6.0-RC.2-KBA-002"
> ```

#### 3.2 Configure Maven Repository

Add or modify the following Maven repository configuration:

```properties
# Maven repository URL
maven_publish_url=https://xxxx/repository/maven/xxx

# Maven credentials
maven_username=user_A
maven_password=password_A
```

### 4. Publish to Maven

After Gradle sync completes, navigate to the kotlinx.datetime project root directory and execute the publish command:

**Option A: Publish to Remote Maven Repository**

```bash
./gradlew publish
```

**Option B: Publish to Local Maven Repository**

If you want to publish to local Maven repository for testing or local development, no additional configuration is required. Simply run:

```bash
./gradlew publishToMavenLocal
```

After publishing locally, add `mavenLocal()` to your project's `settings.gradle.kts`:

```kotlin
dependencyResolutionManagement {
    repositories {
        mavenLocal()
        // other repositories...
    }
}
```
