# mleng-dvc

   Для задачи датасет titanic 
   Пайплайн состоит из следующих этапов
   
   ## preprocess
   файл preprocess.dvc
  ## split
  разделение данных на train и test
  ## logistic_regression
  файл log_regression.dvc
  обучение логистической регресси для предсказания выживаемости 
  ## evaluate.dvc
  расчет метрики roc-auc \
  для обученной модели   \
  для воспроизведения надо склонировать этот репозиторий \
  $git clone https://github.com/Ivanpuzako/mleng-dvc.git \
  $cd mleng-dvc \
  должен быть установлен dvc \
  нужно скачать данные из хранилища \
  $dvc pull data/data.csv.dvc \
  воспроизвести пайплайн нужно командой ниже. В результате появятся разбитые и предобработанные данные в папке data \
  Также будут посчитаны метрики \
  $dvc repro evaluate.dvc \
  
  Был создан эксперимент в ветке regularization-experiment, там было изменено значение регуляризации модели. \
  Для воспроизведения нужно перейти на другую ветку и воспроизвести пайплайн \
  $git checkout regularization-experiment \
  $dvc repro evaluate.dvc \
  
  Для того чтобы помотреть и сравнить метрики можно ввести \
  $dvc metrics show -T
   
   
   
   
   
   
   
   
   
