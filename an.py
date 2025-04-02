import sys
import pandas as pd
import numpy as np
from PySide6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, 
                              QVBoxLayout, QLabel, QMessageBox)
from PySide6.QtCharts import (QChart, QChartView, QLineSeries, QScatterSeries, 
                             QBarSeries, QBarSet, QPieSeries, QValueAxis, QBarCategoryAxis)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Визуализация данных")
        self.setGeometry(100, 100, 1000, 800)
        
        self.tabs = QTabWidget()
        
        # Создаем вкладки
        self.create_sin_cos_tab()
        self.create_trees_tab()
        self.create_hurricanes_tab()
        
        self.setCentralWidget(self.tabs)
    
    def create_sin_cos_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # График синуса
        sin_chart = QChart()
        sin_chart.setTitle("График синуса")
        
        sin_series = QLineSeries()
        sin_series.setName("sin(x)")
        
        x = np.linspace(0, 2*np.pi, 30)
        y_sin = np.sin(x)
        
        for i in range(len(x)):
            sin_series.append(x[i], y_sin[i])
        
        sin_chart.addSeries(sin_series)
        
        # Настройка осей для синуса
        axis_x = QValueAxis()
        axis_x.setTitleText("x (радианы)")
        axis_x.setLabelFormat("%.1f")
        sin_chart.addAxis(axis_x, Qt.AlignBottom)
        sin_series.attachAxis(axis_x)
        
        axis_y = QValueAxis()
        axis_y.setTitleText("sin(x)")
        axis_y.setLabelFormat("%.1f")
        sin_chart.addAxis(axis_y, Qt.AlignLeft)
        sin_series.attachAxis(axis_y)
        
        sin_chart_view = QChartView(sin_chart)
        sin_chart_view.setRenderHint(QPainter.Antialiasing)
        
        # График косинуса
        cos_chart = QChart()
        cos_chart.setTitle("График косинуса")
        
        cos_series = QLineSeries()
        cos_series.setName("cos(x)")
        cos_series.setColor(QColor("orange"))
        
        y_cos = np.cos(x)
        
        for i in range(len(x)):
            cos_series.append(x[i], y_cos[i])
        
        cos_chart.addSeries(cos_series)
        
        # Настройка осей для косинуса
        axis_x = QValueAxis()
        axis_x.setTitleText("x (радианы)")
        axis_x.setLabelFormat("%.1f")
        cos_chart.addAxis(axis_x, Qt.AlignBottom)
        cos_series.attachAxis(axis_x)
        
        axis_y = QValueAxis()
        axis_y.setTitleText("cos(x)")
        axis_y.setLabelFormat("%.1f")
        cos_chart.addAxis(axis_y, Qt.AlignLeft)
        cos_series.attachAxis(axis_y)
        
        cos_chart_view = QChartView(cos_chart)
        cos_chart_view.setRenderHint(QPainter.Antialiasing)
        
        layout.addWidget(sin_chart_view)
        layout.addWidget(cos_chart_view)
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Синус и косинус")
    
    def create_trees_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        try:
            # Загрузка данных о деревьях
            trees = pd.read_csv('trees.csv')
            
            # Проверка структуры данных
            if not all(col in trees.columns for col in ['Girth', 'Height', 'Volume']):
                raise ValueError("Файл trees.csv имеет неверную структуру")
            
            # Точечная диаграмма: Girth vs Height
            scatter_chart = QChart()
            scatter_chart.setTitle("Зависимость высоты дерева от его обхвата")
            
            scatter_series = QScatterSeries()
            scatter_series.setName("Деревья")
            scatter_series.setMarkerSize(10)
            
            for _, row in trees.iterrows():
                scatter_series.append(row["Girth"], row["Height"])
            
            scatter_chart.addSeries(scatter_series)
            
            # Настройка осей для точечной диаграммы
            axis_x = QValueAxis()
            axis_x.setTitleText("Обхват дерева (дюймы)")
            scatter_chart.addAxis(axis_x, Qt.AlignBottom)
            scatter_series.attachAxis(axis_x)
            
            axis_y = QValueAxis()
            axis_y.setTitleText("Высота дерева (футы)")
            scatter_chart.addAxis(axis_y, Qt.AlignLeft)
            scatter_series.attachAxis(axis_y)
            
            scatter_view = QChartView(scatter_chart)
            scatter_view.setRenderHint(QPainter.Antialiasing)
            
            # Столбчатая диаграмма: средний Volume по Girth (округленный)
            bar_chart = QChart()
            bar_chart.setTitle("Средний объем дерева в зависимости от обхвата")
            
            bar_series = QBarSeries()
            
            trees["Girth_rounded"] = trees["Girth"].round().astype(int)
            grouped = trees.groupby("Girth_rounded")["Volume"].mean()
            
            categories = []
            for girth, volume in grouped.items():
                bar_set = QBarSet(str(girth))
                bar_set.append(volume)
                bar_series.append(bar_set)
                categories.append(str(girth))
            
            bar_chart.addSeries(bar_series)
            
            # Настройка осей для столбчатой диаграммы
            axis_x = QBarCategoryAxis()
            axis_x.setTitleText("Обхват дерева (дюймы, округленные)")
            axis_x.append(categories)
            bar_chart.addAxis(axis_x, Qt.AlignBottom)
            bar_series.attachAxis(axis_x)
            
            axis_y = QValueAxis()
            axis_y.setTitleText("Средний объем (кубические футы)")
            bar_chart.addAxis(axis_y, Qt.AlignLeft)
            bar_series.attachAxis(axis_y)
            
            bar_view = QChartView(bar_chart)
            bar_view.setRenderHint(QPainter.Antialiasing)
            
            layout.addWidget(scatter_view)
            layout.addWidget(bar_view)
            
        except Exception as e:
            self.show_error_message(tab, layout, str(e), "Ошибка загрузки данных о деревьях")
        
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Деревья")
    
    def create_hurricanes_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        try:
            # Загрузка данных об ураганах
            hurricanes = pd.read_csv('hurricanes.csv')
            
            # Проверка структуры данных
            required_columns = ['Month', 'Average']
            year_columns = [col for col in hurricanes.columns if col not in required_columns]
            
            if not all(col in hurricanes.columns for col in required_columns) or len(year_columns) == 0:
                raise ValueError("Файл hurricanes.csv имеет неверную структуру")
            
            # Круговая диаграмма для 2007 года
            if '2007' in hurricanes.columns:
                pie_2007 = QChart()
                pie_2007.setTitle("Распределение ураганов 2007 года по месяцам")
                
                pie_series_2007 = QPieSeries()
                
                # Находим максимальное значение для выделения
                max_value = hurricanes['2007'].max()
                
                for _, row in hurricanes.iterrows():
                    if row['2007'] > 0:
                        slice_ = pie_series_2007.append(row['Month'], row['2007'])
                        if row['2007'] == max_value:
                            slice_.setExploded(True)
                            slice_.setLabelVisible(True)
                
                pie_2007.addSeries(pie_series_2007)
                
                pie_view_2007 = QChartView(pie_2007)
                pie_view_2007.setRenderHint(QPainter.Antialiasing)
                
                layout.addWidget(pie_view_2007)
            else:
                raise ValueError("Отсутствуют данные за 2007 год")
            
            # Круговая диаграмма по годам
            pie_years = QChart()
            pie_years.setTitle("Распределение ураганов по годам")
            
            pie_series_years = QPieSeries()
            
            yearly_totals = hurricanes[year_columns].sum()
            
            # Находим минимальное значение для выделения
            min_value = yearly_totals.min()
            
            for year, total in yearly_totals.items():
                slice_ = pie_series_years.append(year, total)
                if total == min_value:
                    slice_.setExploded(True)
                    slice_.setLabelVisible(True)
            
            pie_years.addSeries(pie_series_years)
            
            pie_view_years = QChartView(pie_years)
            pie_view_years.setRenderHint(QPainter.Antialiasing)
            
            layout.addWidget(pie_view_years)
            
        except Exception as e:
            self.show_error_message(tab, layout, str(e), "Ошибка загрузки данных об ураганах")
        
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Ураганы")
    
    def show_error_message(self, tab, layout, error, title):
        error_label = QLabel(f"Ошибка: {error}")
        error_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(error_label)
        
        # Показываем сообщение об ошибке
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(error)
        msg.setWindowTitle(title)
        msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())