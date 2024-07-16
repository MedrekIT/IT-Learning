#include <QApplication>
#include "OknoGlowne.h"

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    OknoGlowne w;
    w.show();
    return app.exec();
}
