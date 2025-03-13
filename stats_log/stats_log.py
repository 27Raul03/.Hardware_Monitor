    # def export_weekly_summary(self):
    #     """Generate and export a weekly summary of the log data."""
    #     log_path = os.path.abspath("logs/hardware_log.csv")
    #     if not os.path.exists(log_path):
    #         QMessageBox.warning(self, "Error", "Log file not found.")
    #         return

    #     end_date = datetime.now()
    #     start_date = end_date - timedelta(days=7)

    #     weekly_data = []
    #     with open(log_path, 'r') as log_file:
    #         reader = csv.reader(log_file)
    #         for row in reader:
    #             timestamp = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
    #             if start_date <= timestamp <= end_date:
    #                 weekly_data.append(row)

    #     if not weekly_data:
    #         QMessageBox.warning(self, "Error", "No data found for the past week.")
    #         return

    #     cpu_usage = [float(row[1]) for row in weekly_data]
    #     ram_usage = [float(row[4]) for row in weekly_data]
    #     disk_usage = [float(row[5]) for row in weekly_data]

    #     summary = {
    #         "start_date": start_date.strftime('%Y-%m-%d'),
    #         "end_date": end_date.strftime('%Y-%m-%d'),
    #         "avg_cpu_usage": sum(cpu_usage) / len(cpu_usage),
    #         "max_cpu_usage": max(cpu_usage),
    #         "avg_ram_usage": sum(ram_usage) / len(ram_usage),
    #         "max_ram_usage": max(ram_usage),
    #         "avg_disk_usage": sum(disk_usage) / len(disk_usage),
    #         "max_disk_usage": max(disk_usage),
    #     }

    #     summary_path = os.path.abspath("logs/weekly_summary.csv")
    #     with open(summary_path, 'w', newline='') as summary_file:
    #         writer = csv.writer(summary_file)
    #         writer.writerow(["Metric", "Value"])
    #         writer.writerow(["Start Date", summary["start_date"]])
    #         writer.writerow(["End Date", summary["end_date"]])
    #         writer.writerow(["Average CPU Usage (%)", summary["avg_cpu_usage"]])
    #         writer.writerow(["Max CPU Usage (%)", summary["max_cpu_usage"]])
    #         writer.writerow(["Average RAM Usage (%)", summary["avg_ram_usage"]])
    #         writer.writerow(["Max RAM Usage (%)", summary["max_ram_usage"]])
    #         writer.writerow(["Average Disk Usage (%)", summary["avg_disk_usage"]])
    #         writer.writerow(["Max Disk Usage (%)", summary["max_disk_usage"]])

    #     QMessageBox.information(self, "Success", f"Weekly summary exported to {summary_path}")