# kotlinx.serialization

本补丁基于官方 kotlinx.serialization 1.7.1 版本（commit d2f7316e）构建，用于支持 OpenHarmony 平台。

## 快速开始

### 1. 添加 Maven 仓库

在项目的 `settings.gradle.kts` 中添加腾讯 Maven 仓库：

```kotlin
dependencyResolutionManagement {
    repositories {
        maven {
            url = uri("https://mirrors.tencent.com/nexus/repository/maven-tencent/")
        }
    }
}
```

### 2. 添加依赖

在模块的 `build.gradle.kts` 中添加依赖：

```kotlin
// Serialization 依赖
implementation("org.jetbrains.kotlinx:kotlinx-serialization-core:1.7.1-KBA-003")
implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.1-KBA-003")
```

特别地，如果要在鸿蒙系统（OpenHarmony）上使用，需要在 `build.ohos.gradle.kts` 中添加依赖：

```kotlin
// Serialization 依赖
implementation("org.jetbrains.kotlinx:kotlinx-serialization-core:1.7.1-KBA-003")
implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.1-KBA-003")
```

---

## 如何发布

### 1. 下载 kotlinx.serialization

克隆官方 kotlinx.serialization 项目到本地：

```bash
git clone https://github.com/Kotlin/kotlinx.serialization.git
```

切换到 commit d2f7316e 并创建新分支：

```bash
git checkout -b v1.7.1 d2f7316e
```

### 2. 应用补丁

将补丁文件下载到项目根目录，并应用补丁：

```bash
git apply serialization.patch
```

### 3. 配置 Maven 设置

#### 3.1 修改版本号

找到并更新版本属性为你需要的版本：

```kotlin
version = "1.7.1-ohos-1.0.0"
```

#### 3.2 配置 Maven 仓库

将以下 `username`、`password` 和 `url` 替换为你的 Maven 仓库信息：

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

### 4. 发布到 Maven

Gradle 同步完成后，进入 kotlinx.serialization 项目根目录，执行发布命令：

**方式 A：发布到远程 Maven 仓库**

```bash
./gradlew publish
```

**方式 B：发布到本地 Maven 仓库**

如果要发布到本地 Maven 仓库进行测试或本地开发，无需额外配置，直接运行：

```bash
./gradlew publishToMavenLocal
```

发布到本地后，在项目的 `settings.gradle.kts` 中添加 `mavenLocal()`：

```kotlin
dependencyResolutionManagement {
    repositories {
        mavenLocal()
        // 其他仓库...
    }
}
```
