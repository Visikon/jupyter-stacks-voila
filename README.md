# Visikon notes

This repo is a fork of https://github.com/torressa/jupyter-stacks-voila.

The docker files is polluted with paths from his local machine, as well as undocumented environment variables.
I haven't changed any of that, as the notebook works, but we may want to improve it in the future.

Build and run the jupyter server using the following command.

```bash
cd scripts/
./run_notebook
```

Open the url in the browser at http://127.0.0.1:8888/lab/ and use the token from the command line output to log in
```
docker-run-notebook-1  | [I 2022-10-12 08:26:46.114 ServerApp] Jupyter Server 1.19.1 is running at:
docker-run-notebook-1  | [I 2022-10-12 08:26:46.114 ServerApp] http://d3a88d0f3bd3:8888/lab?token=db779534b84b38848f5d45222f79d04cca8f74d50b2585f9
docker-run-notebook-1  | [I 2022-10-12 08:26:46.114 ServerApp]  or http://127.0.0.1:8888/lab?token=db779534b84b38848f5d45222f79d04cca8f74d50b2585f9
docker-run-notebook-1  | [I 2022-10-12 08:26:46.114 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
docker-run-notebook-1  | [C 2022-10-12 08:26:46.116 ServerApp]
docker-run-notebook-1  |
docker-run-notebook-1  |     To access the server, open this file in a browser:
docker-run-notebook-1  |         file:///home/jovyan/.local/share/jupyter/runtime/jpserver-7-open.html
docker-run-notebook-1  |     Or copy and paste one of these URLs:
docker-run-notebook-1  |         http://d3a88d0f3bd3:8888/lab?token=db779534b84b38848f5d45222f79d04cca8f74d50b2585f9
docker-run-notebook-1  |      or http://127.0.0.1:8888/lab?token=db779534b84b38848f5d45222f79d04cca8f74d50b2585f9
```

The notebooks are kept in a volume mapped to: [notebooks/](notebooks/)

Run the notebook as a dashboard by choosing `View/Open with voila in New Browser Tab` and auto refresh using this chrome extension: https://chrome.google.com/webstore/detail/auto-refresh-plus-page-mo/hgeljhfekpckiiplhkigfehkdpldcggm/related

### Future enhancements
- The notebooks can be run in stand-alone mode using the `./deploy_notebook`, which starts a `voila` server and exposes it on port 80 using an nginx container. this doesn't work on my machine, most likely because of the issues mentioned in the beginning.
- The auto refresh can be implemented using the jupyter extension https://github.com/jupyter-server/jupyter-scheduler, but the browser addon soluiton is simpler
- A widget based dashboard can be built, using the jupyter extension https://github.com/voila-dashboards/voila-gridstack

# Original notes
## jupyter-stacks-voila

(Minimal) working example to learn how to deploy a jupyter notebook
(ran on [jupyter/docker-stacks](https://github.com/jupyter/docker-stacks))
using [voila](https://github.com/voila-dashboards/voila/tree/stable) and [nginx](https://docs.nginx.com/).

## Requirements

- Docker and docker-compose
- bash

##  Quick start

To run and edit the notebooks in `notebooks/` on a jupyter/docker-stacks container
(in case you don't have jupyter locally)

```bash
cd scripts/
./run_notebook
```

To serve your notebook on voila through nginx on `http://localhost:80`,

```bash
cd scripts/
./deploy_notebook
```

## Structure

- [`data/`](data/) - folder with data that is mounted and used inside the notebook. Contains a test csv file with the iris data set.
- [`docker/`](docker/) - all necessary docker and docker-compose files.
- [`my_module/`](my_module/) - some python module that is required in the notebook.
- [`nginx/conf.d/`](nginx/conf.d/) - configuration files for nginx.
- [`notebooks/`](notebooks/) - jupyter notebook to show.
- [`scripts/`](scripts/) - bash scripts to docker-compose up the necessary stuff.

Please see the [docs](docs/) for more information.
