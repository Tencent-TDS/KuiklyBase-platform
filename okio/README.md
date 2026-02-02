# okio

This patch is built on the official okio version 3.9.10 (commit c43c9a61) to support platform OpenHarmony.

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
implementation("com.squareup.okio:okio:3.9.10-KBA-001")
```

Specifically, if you want to use it on the HarmonyOS (OpenHarmony) platform, you need to add the dependency in `build.ohos.gradle.kts`:

```kotlin
implementation("com.squareup.okio:okio:3.9.10-KBA-001")
```

---

## How to Publish

### 1. Download okio

Clone the official okio project locally:

```bash
git clone https://github.com/square/okio
```

Checkout commit c43c9a61 and create a new branch:

```bash
git checkout -b 3.9.10-KBA-001 c43c9a61
```

### 2. Apply Patch

Download the patch file to the project root directory and apply it:

```bash
git apply okio.patch
```

### 3. Configure gradle.properties

Open `gradle.properties` file to configure the version number and Maven repository settings.

#### 3.1 Modify Version Number

Find and update the version property to your desired version:

```properties
version=3.9.10-ohos-1.0.0
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

After Gradle sync completes, navigate to the okio project root directory and execute the publish command:

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
