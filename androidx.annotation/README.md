# androidx.annotation

This patch is built on the official androidx.annotation version 1.8.0 to support OpenHarmony platform.

---

# Part 1: Quick Start

## 1. Add Maven Repository

Add the remote repository in your project's `settings.gradle.kts`:

```kotlin
dependencyResolutionManagement {
    repositories {
        maven {
            url = uri("https://mirrors.tencent.com/nexus/repository/maven-tencent/")
        }
    }
}
```

## 2. Add Dependencies

Add the following dependency in your `commonMain` module's `build.gradle.kts`:

```kotlin
implementation("androidx.annotation:annotation:1.8.0-KBA-002")
```

---

# Part 2: Build from Source

## 1. Clone AOSP Support Repository

Clone the Google AOSP support project:

```bash
git clone https://android.googlesource.com/platform/frameworks/support
```

Checkout the specific commit:

```bash
git checkout 4e5e9e3ddec39fb6f9f34c89b1b4f9b58a1ab627
```

## 2. Apply Patch

Download [ov-androidx.annotation-1.8.0.patch](ov-androidx.annotation-1.8.0.patch) and apply it:

```bash
git apply ov-androidx.annotation-1.8.0.patch
```

## 3. Configure Maven Repository

Add remote maven repositories in `buildSrc/repos.gradle`:

```groovy
handler.maven {
    url = "https://mirrors.tencent.com/nexus/repository/maven-public"
}
handler.maven {
    url = "https://mirrors.tencent.com/nexus/repository/maven-tencent"
}
```

Configure maven publish settings in `playground-common/androidx-shared.properties`:

```properties
maven.remote.url=https://your-maven-repo-url
maven.remote.username=your_username
maven.remote.password=your_password
```

Update the annotation version in `libraryversions.toml`:

```toml
ANNOTATION=1.8.0-KBA-002
```

## 4. Publish

**Requirements:** JDK 21

Navigate to the project root and run:

```bash
cd playground-projects/collection-playground
./gradlew studio
```

After syncing, run the publishing gradle task in Android Studio to deploy the annotation artifacts.