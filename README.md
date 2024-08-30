# Example Project for Using Dagster in Data Operations

This repository contains an example project that accompanies a blog post outlining how to effectively use Dagster for
data operations, focusing on reading and writing data with the proper use of resources and IO managers.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

This project serves as a practical example demonstrating how to set up and utilize Dagster for data processing tasks,
including:

- Structuring clean and maintainable Dagster pipelines.
- Reading and writing data efficiently.
- Utilizing resources and IO managers for flexible data operations.

The Makefile included simplifies the setup and execution of common tasks within the project.

## Installation

To get started with this project, follow these steps:

1. **Clone the repository:**

```bash
git clone https://yourrepo.com/example-dagster-project.git
cd dagster-blogpost-repo
```

2. **Create a virtual environment:**

```make
make venv
source venv/bin/activate
```

3. **Install dependencies:**

```make
make install-pip-tools
```

```make
make compile-dependencies
```

```make
make install-dependencies-base
```

## Usage

After installation, you can use the Makefile commands to interact with the project:

- **Get a proper .env file**
  Rename `.env.example` to .env or copy its content to a new file named `.env`.

- **Create a dagster_home folder**
- Create a new directory in root named `dagster_home` via

```bash
mkdir dagster_home
```

In this folder, dagster stores logs, historical runs, etc. Copy the absolute path to this folder into the `.env` file
and put it next to `DAGSTER_HOME=/your/path/to/dagster_home`.

- **Start the locally hosted MinIO S3 instance via**

```bash
docker compose up -d
```

In the CLI output you should see a section like

`dagster-blogpost-repo-minio-1 | Status:         1 Online, 0 Offline.`

`dagster-blogpost-repo-minio-1 | S3-API: http://111.11.0.1:port  http://111.1.1.1:port`

The second S3-API link will open MINIO in your browser. Go ahead and fill in the `MINIO_ROOT_USER` and
the `MINIO_ROOT_PASSWORD` stored in your `.env` file.

Do not forget to tear the MinIO S3 Docker container down when you are done via

```bash
docker compose down
```

- **Start the Dagster UI for development:**

```make
make dagster_ui
```

Once the Dagster UI is set-up you can access it in your browser and start jobs interactively. Of course you can start
all of the jobs as well via the command line as follows

- **Execute the preprocessing job:**

```make
make preprocessing_job
```

- **Execute the training job:**

```make
make training_job
```

For a detailed explanation of each step and how to use Dagster for data operations, refer to the accompanying blog post.

## Contributing

We welcome contributions! Please open an issue or submit a pull request for any enhancements, bug fixes, or
improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or comments about this project, please open an issue in the repository, and we'll get back to you as
soon as possible.
