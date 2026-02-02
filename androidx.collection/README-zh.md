# androidx.collection

本补丁基于官方 androidx.collection 1.4.0 版本构建，用于支持 OpenHarmony 平台。

---

# 快速接入

## 1. 添加 Maven 仓库

在项目的 `settings.gradle.kts` 中添加远程仓库：

```kotlin
dependencyResolutionManagement {
    repositories {
        maven {
            url = uri("https://mirrors.tencent.com/nexus/repository/maven-tencent/")
        }
    }
}
```

## 2. 添加依赖

在 `commonMain` 模块的 `build.gradle.kts` 中添加以下依赖：

```kotlin
implementation("androidx.collection:collection:1.4.0-KBA-001")
```

---

# 从源码构建发布

## 1. 克隆 AOSP Support 仓库

克隆 Google AOSP support 项目：

```bash
git clone https://android.googlesource.com/platform/frameworks/support
```

切换到指定的 commit：

```bash
git checkout 6bb3d4c5410cf394070cca4ff347d46454194480
```

## 2. 应用补丁

下载 [ov-androidx.collection-1.4.0.patch](ov-androidx.collection-1.4.0.patch) 并应用：

```bash
git apply ov-androidx.collection-1.4.0.patch
```

## 3. 配置 Maven 仓库

在 `buildSrc/repos.gradle` 中添加远程 Maven 仓库：

```groovy
handler.maven {
    url = "https://mirrors.tencent.com/nexus/repository/maven-public"
}
handler.maven {
    url = "https://mirrors.tencent.com/nexus/repository/maven-tencent"
}
```

在 `playground-common/androidx-shared.properties` 中配置 Maven 发布信息：

```properties
maven.remote.url=https://your-maven-repo-url
maven.remote.username=your_username
maven.remote.password=your_password
```

在 `libraryversions.toml` 中更新 collection 版本号：

```toml
COLLECTION=XXX
```

## 4. 发布

**环境要求：** JDK 21

进入项目根目录并执行：

```bash
cd playground-projects/collection-playground
./gradlew publish --dependency-verification=off
```

同步完成后，在 Android Studio 中运行发布 Gradle 任务来部署 collection 产物。
