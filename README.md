## Oshe

### What
Oshe is a tasker of web crawler.

### Feature
1. Flexible
Oshe divides the crawling process into three steps: crawl, parse and store.
Each step is individual, and can be replaced by other implementations.

2. Distributable
With the help of celery, each step can be distributed to several machine.

### Requirements
Oshe is currently developed on ubuntu 16.04 in Python 3.5.2.

### How
Type `oshe --help` to get all available commands.

`oshe init`: init an project under current directory, with an demo app to demonstrate how to use oshe.
`oshe create app_name`: create an app named `app_name` under the `project` directory.
`oshe worker`: start celery worker in the machine where the command is executed. Workers must be started before any
crawl tasks can be executed.
`oshe beat`: start celery beat, which is necessary to execute periodic crawl task.
`oshe deploy environment`: deploy project to `environment`.
`oshe test`: test oshe framework, for developers only.

### Plan
1. support phantomjs crawler.
2. better support to balance crawl, parse and store queue.
3. better method to organize task chain.