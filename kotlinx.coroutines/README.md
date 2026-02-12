# kotlinx.coroutines

This patch is built on the official kotlinx.coroutines version 1.8.0 to support platform OpenHarmony.

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
implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.8.0-KBA-001")
```

Specifically, if you want to use it on the HarmonyOS (OpenHarmony) platform, you need to add the dependency in `build.ohos.gradle.kts`:

```kotlin
implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.8.0-KBA-001")
```

---

## How to Publish

### 1. Download kotlinx.coroutines

Clone the official kotlinx.coroutines project locally:

```bash
git clone https://github.com/Kotlin/kotlinx.coroutines.git
```

Checkout tag 1.8.0 and create a new branch:

```bash
git checkout -b v1.8.0 1.8.0
```

### 2. Apply Patch

Download the patch file to the project root directory and apply it:

```bash
git apply kotlinx-coroutines.patch
```

### 3. Configure gradle.properties

Open `gradle.properties` file to configure the version number and Maven repository settings.

#### 3.1 Modify Version Number

Find and update the version property to your desired version:

```properties
version=1.8.0-ohos-1.0.0
```

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

After Gradle sync completes, navigate to the kotlinx.coroutines project root directory and execute the publish command:

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
