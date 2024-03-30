# data-engineering-project
This repo contains the project for the [Data Engineering Zoomcamp 2024 by Datatalks.Club](https://github.com/DataTalksClub/data-engineering-zoomcamp)

## Project
Building a data engineering pipeline to visualize the indicators, volume and returns of any stock in the Dow Jones Industrial Average index for a given data range.

### Strategy

yahoo api --> gcs (data lake) (mage)
gcs --> bq (data warehouse) (mage)
bq --> bq (transformation) (mage[dbt])
bq --> dashboard (powerbi/looker)

### Prerequisities

Install docker, docker-compose, terraform, git, any IDE, GCP account.

# Steps to Follow:

1.  Clone the repository: git clone git@github.com:heman2002/data-engineering-project.git

2.  Create your google cloud account with a project and service details and download the service details json file.

3.  Save your gcp key to the mage directory and the terraform directory.

4.  cd terraform
    Update the variables.tf with gcp info like variable "credentials", "project", "region", "location", "bq_dataset_name", "gcs_bucket_name"

5.  terraform init
    terraform plan
    terraform apply 
    
6.  cd mage
    docker-compose build
    docker-compose up

    After the server starts, open localhost:6789 in your browser and select pipelines -> djia_pipeline. Go to last block on the pipeline and click on run with all upstream blocks.

    Now, your pipeline will run various load, transform and export blocks one after the other.

7. Once the project is complete.
    docker-compose down 
    terraform destroy