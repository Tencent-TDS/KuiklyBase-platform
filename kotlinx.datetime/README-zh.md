# kotlinx.datetime

本补丁基于官方 kotlinx.datetime 0.6.0-RC.2 版本构建，用于支持 OpenHarmony 平台。

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
implementation("org.jetbrains.kotlinx:kotlinx-datetime:0.6.0-RC.2-KBA-003")
```

特别地，如果要在鸿蒙系统（OpenHarmony）上使用，需要在 `build.ohos.gradle.kts` 中添加依赖：

```kotlin
implementation("org.jetbrains.kotlinx:kotlinx-datetime:0.6.0-RC.2-KBA-003")
```

---

## 平台特定说明

### 鸿蒙系统 (OpenHarmony)

在鸿蒙项目中添加时区依赖：

```json
"dependencies": {
    "@kuiklybase/timezone": "0.0.1"
}
```

在代码中进行初始化（必须，否则会崩溃）：

```typescript
import "@kuiklybase/timezone"
```

### Android

datetime 库与低 API 级别的设备不兼容。为了解决这个问题，我们引入了 `com.jakewharton.threetenabp:threetenabp:1.4.7`。

对于 Android，确保在应用启动时进行初始化：

```kotlin
AndroidThreeTen.init(application)
```

---

## 如何发布

### 1. 下载 kotlinx.datetime

克隆官方 kotlinx.datetime 项目到本地：

```bash
git clone https://github.com/Kotlin/kotlinx-datetime.git
```

切换到 0.6.0-RC.2 标签并创建新分支：

```bash
git checkout -b v0.6.0-RC.2 v0.6.0-RC.2
```

### 2. 应用补丁

将补丁文件下载到项目根目录，并应用补丁：

```bash
git apply kotlinx-datetime.patch
```

### 3. 配置 gradle.properties

打开 `gradle.properties` 文件，配置版本号和 Maven 仓库设置。

#### 3.1 修改版本号

找到并更新版本属性为你需要的版本：

```properties
version=0.6.0-RC.2-ohos-1.0.0
```

> **注意**：源码中 `core/build.gradle.kts`（第 20 行）存在硬编码的版本号。如果修改版本号后未生效，请检查 `core/build.gradle.kts` 文件，删除或注释掉硬编码的版本号：
>
> ```kotlin
> // 如果存在这行，请删除或注释掉
> version = "0.6.0-RC.2-KBA-002"
> ```

#### 3.2 配置 Maven 仓库

添加或修改以下 Maven 仓库配置：

```properties
# Maven 仓库地址
maven_publish_url=https://xxxx/repository/maven/xxx

# Maven 凭证
maven_username=user_A
maven_password=password_A
```

### 4. 发布到 Maven

Gradle 同步完成后，进入 kotlinx.datetime 项目根目录，执行发布命令：

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
