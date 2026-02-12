# androidx.lifecycle

本补丁基于官方 androidx.lifecycle 2.8.0 版本构建，用于支持 OpenHarmony 平台。

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
implementation("androidx.lifecycle:lifecycle-common:2.8.0-KBA-002")
implementation("androidx.lifecycle:lifecycle-runtime:2.8.0-KBA-002")
implementation("androidx.lifecycle:lifecycle-viewmodel:2.8.0-KBA-002")
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
git checkout 7ad6b8bbf8fa3d5a3c97feca6c52a1a2bf98a622
```

## 2. 应用补丁

下载 [ov-androidx.lifecycle-2.8.0.patch](ov-androidx.lifecycle-2.8.0.patch) 并应用：

```bash
git apply ov-androidx.lifecycle-2.8.0.patch
```

## 3. 配置 Maven 仓库

在 `buildSrc/repos.gradle` 中添加远程 Maven 仓库，用于获取构建发布时需要的依赖：

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

在 `libraryversions.toml` 中更新 lifecycle 版本号：

```toml
LIFECYCLE=XXX
```

## 4. 发布

**环境要求：** JDK 21

进入项目根目录并执行：

```bash
cd playground-projects/lifecycle-playground
./gradlew publish --dependency-verification=off
```