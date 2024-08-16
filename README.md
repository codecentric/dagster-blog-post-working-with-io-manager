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

git clone https://yourrepo.com/example-dagster-project.git
cd example-dagster-project

2. **Create a virtual environment:**
```make
make venv
source venv/bin/activate
```

3. **Install dependencies:**
```make
make install-pip-tools
make compile-dependencies
make install-dependencies-base
```

## Usage

After installation, you can use the Makefile commands to interact with the project:

- **Start the locally hosted MinIO S3 instance via

```bash
docker-compose up
```

- **Start the Dagster UI for development:**

```make
make dagster_ui
```

- **Execute the preprocessing job:**

```make
make preprocessing_job
```

- **Execute the training job:**

```make
make training
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
