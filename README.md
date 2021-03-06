[![Waffle.io - Columns and their card count](https://badge.waffle.io/arts-in-motion/arts-in-motion.png?columns=backlog,current,review)](https://waffle.io/arts-in-motion/arts-in-motion?utm_source=badge)
[![CircleCI](https://circleci.com/gh/arts-in-motion/arts-in-motion.svg?style=svg)](https://circleci.com/gh/arts-in-motion/arts-in-motion)

# Overview

# Setup

## Requirements

The following must be installed on your system:

- Make
- Python 3.6
- pipenv
- PostgreSQL

To confirm the correct versions are installed:

```
$ make doctor
```

## Setup

Create a database:

```sh
$ createdb artsinmotion_dev
```

Install project dependencies:

```
$ make install
```

Run migrations and generate test data:

```
$ make data
```

## Development

Run the application and recompile static files:

```
$ make run
```

Continuously run validation targets:

```
$ make watch
```

or run them individually:

```
$ make check
$ make test-unit
$ make test-integration
$ make test-system
```
