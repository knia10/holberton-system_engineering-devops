# 0x17. Web stack debugging #3
## Background Context π
<img src = "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/293/d42WuBh.png" width = 400px length = 300px>

When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)

Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websitesβ¦ It [actually powers 26% of the web](https://managewp.com/blog/statistics-about-wordpress-usage), so there is a fair chance that you will end up working with it at some point in your career.

Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.

The web stack you are debugging today is a Wordpress website running on a LAMP stack.

## Requirements
### General
- π© All your files will be interpreted on Ubuntu 14.04 LTS
- π© All your files should end with a new line
- π© A `README.md` file at the root of the folder of the project is mandatory
- π© Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors
- π© Your Puppet manifests must run without error
- π© Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- π© Your Puppet manifests files must end with the extension `.pp`
- π© Files will be checked with Puppet v3.4


## More Info π
**Install** `puppet-lint`
```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```
By Estefani Ruiz π¦ From Holberton School πͺ