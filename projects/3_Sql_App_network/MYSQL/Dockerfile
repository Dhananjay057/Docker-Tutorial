# Pull the MYSQL base image
FROM mysql:8.0

#Set the environment variables for MYSQL
ENV MYSQL_ROOT_PASSWORD=demopassword    
ENV MYSQL_DATABASE=demodb

# Copy the initialisation SQL script to the container
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the default MYSQL port
EXPOSE 3307
 
#
