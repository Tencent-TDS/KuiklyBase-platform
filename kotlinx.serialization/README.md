# kotlinx.serialization

This patch is built on the official kotlinx.serialization version 1.7.1 (commit d2f7316e) to support platform OpenHarmony.

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
implementation("org.jetbrains.kotlinx:kotlinx-serialization-core:1.7.1-KBA-003")
implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.1-KBA-003")```

Specifically, if you want to use it on the HarmonyOS (OpenHarmony) platform, you need to add the dependency in `build.ohos.gradle.kts`:

```kotlin
implementation("org.jetbrains.kotlinx:kotlinx-serialization-core:1.7.1-KBA-003")
implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.1-KBA-003")```

---

## How to Publish

### 1. Download kotlinx.serialization

Clone the official kotlinx.serialization project locally:

```bash
git clone https://github.com/Kotlin/kotlinx.serialization.git
```

Checkout commit d2f7316e and create a new branch:

```bash
git checkout -b v1.7.1 d2f7316e
```

### 2. Apply Patch

Download the patch file to the project root directory and apply it:

```bash
git apply serialization.patch
```

### 3. Configure Maven Settings

#### 3.1 Modify Version Number

Find and update the version property to your desired version:

```kotlin
version = "1.7.1-ohos-1.0.0"
```

#### 3.2 Configure Maven Repository

Replace the following `username`, `password`, and `url` with your Maven repository information:

```kotlin
fun configureMavenPublication(rh: RepositoryHandler, project: Project) {
    rh.maven {
        url = uri("https://xxxx/repository/maven/xxx")
        credentials {
            username = "user_A"
            password = "password_A"
        }
    }
}
```

### 4. Publish to Maven

After Gradle sync completes, navigate to the kotlinx.serialization project root directory and execute the publish command:

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
